# -*- coding: utf-8 -*-
"""State management for TCM study reminder system."""

import json
import datetime
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

STATE_FILE = r"D:\dong_y_reminder\state.json"

PHASE_DURATIONS = [8, 12, 20, 32, 20, 999]

DEFAULT_STATE = {
    "phase_index": 0,
    "phase_start_date": str(datetime.date.today()),
    "mode": "study",
    "quiz_message_id": None,
    "quiz_sent_date": None,
    "failed_attempts": 0,
    "day_index": 0,
    "pending_tasks": [],
    "tasks_log": {},
}


def load_state() -> dict:
    if not os.path.exists(STATE_FILE):
        save_state(DEFAULT_STATE.copy())
        return DEFAULT_STATE.copy()
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Fill missing keys with defaults
    for k, v in DEFAULT_STATE.items():
        data.setdefault(k, v)
    return data


def save_state(state: dict):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def get_days_in_phase(state: dict) -> int:
    start = datetime.date.fromisoformat(state["phase_start_date"])
    return (datetime.date.today() - start).days


def get_phase_duration_weeks(phase_index: int) -> int:
    if phase_index < 0 or phase_index >= len(PHASE_DURATIONS):
        return 999
    return PHASE_DURATIONS[phase_index]


def get_today_tasks(state: dict) -> list:
    """Return list of task strings for today: pending from yesterday + new from curriculum."""
    from curriculum import CURRICULUM
    phase_idx = state.get("phase_index", 0)
    day_index = state.get("day_index", 0)
    pending_indices = state.get("pending_tasks", [])

    curriculum_days = CURRICULUM.get(phase_idx, [])
    if not curriculum_days:
        return []

    # New tasks for today
    safe_day = day_index % len(curriculum_days)
    new_tasks = curriculum_days[safe_day]

    # Pending tasks from yesterday (already stored as strings)
    pending_strings = state.get("_pending_task_strings", [])

    return pending_strings + new_tasks


def advance_day(state: dict, completed_indices: list, tasks_list: list) -> dict:
    """
    Mark completed tasks, update pending, increment day_index.
    completed_indices: 1-based indices the user replied with.
    tasks_list: the full list of tasks sent today (pending + new).
    Returns updated state.
    """
    today_str = str(datetime.date.today())

    # Determine which tasks were done (1-based -> 0-based)
    done_strings = []
    pending_strings = []
    for i, task in enumerate(tasks_list):
        if (i + 1) in completed_indices:
            done_strings.append(task)
        else:
            pending_strings.append(task)

    # Log completed tasks
    if "tasks_log" not in state:
        state["tasks_log"] = {}
    state["tasks_log"][today_str] = done_strings

    # Store pending as strings for tomorrow
    state["_pending_task_strings"] = pending_strings

    # Only advance day_index if ALL tasks completed
    if not pending_strings:
        state["day_index"] = state.get("day_index", 0) + 1

    return state


def is_quiz_time(state: dict) -> bool:
    phase_index = state["phase_index"]
    if phase_index >= 5:
        return False
    days = get_days_in_phase(state)
    duration_days = get_phase_duration_weeks(phase_index) * 7
    return days >= duration_days

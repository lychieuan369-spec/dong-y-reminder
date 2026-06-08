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


def is_quiz_time(state: dict) -> bool:
    phase_index = state["phase_index"]
    if phase_index >= 5:
        return False
    days = get_days_in_phase(state)
    duration_days = get_phase_duration_weeks(phase_index) * 7
    return days >= duration_days

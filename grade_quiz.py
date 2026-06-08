# -*- coding: utf-8 -*-
"""
Grade Quiz — TCM Study Reminder System
Run by Task Scheduler daily at 21:30 when mode=quiz.
Polls Telegram for 8 batches of 20-char answers, grades them, advances or repeats phase.
"""

import os
import sys
import re
import requests
import datetime

sys.stdout.reconfigure(encoding='utf-8')

from state import load_state, save_state, get_phase_duration_weeks, get_today_tasks, advance_day

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8815369190:AAGWX03FTic4lq_J5J8Mqn2xFwE7YhwBxP0")
CHAT_ID   = os.environ.get("CHAT_ID",   "8842938928")

PASS_THRESHOLD = 120   # out of 160
TOTAL_QUESTIONS = 160
BATCH_SIZE = 10
NUM_BATCHES = 16


def send_telegram(text: str) -> bool:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
    }
    try:
        resp = requests.post(url, json=payload, timeout=15)
        return resp.ok
    except Exception as e:
        print(f"[ERROR] Telegram send failed: {e}")
        return False


def get_recent_updates(limit: int = 200):
    """Fetch recent Telegram updates."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    params = {"limit": limit, "timeout": 0}
    try:
        resp = requests.get(url, params=params, timeout=20)
        if resp.ok:
            return resp.json().get("result", [])
    except Exception as e:
        print(f"[ERROR] getUpdates failed: {e}")
    return []


def collect_batch_answers(updates, quiz_sent_date: str):
    """
    Collect up to 8 messages matching ^[ABCDabcd]{10}$ sent after quiz_sent_date.
    Returns list of uppercased strings in chronological order.
    """
    pattern = re.compile(r'^[ABCDabcd]{10}$')
    candidates = []

    try:
        sent_date = datetime.date.fromisoformat(quiz_sent_date)
    except Exception:
        sent_date = datetime.date.today()

    for update in updates:
        msg = update.get("message") or update.get("edited_message")
        if not msg:
            continue
        chat_id = str(msg.get("chat", {}).get("id", ""))
        if chat_id != str(CHAT_ID):
            continue
        text = msg.get("text", "").strip()
        if not pattern.match(text):
            continue
        msg_ts = msg.get("date", 0)
        msg_date = datetime.date.fromtimestamp(msg_ts)
        if msg_date >= sent_date:
            candidates.append((msg_ts, text.upper()))

    # Sort chronologically
    candidates.sort(key=lambda x: x[0])

    # Deduplicate by timestamp, keep first occurrence per timestamp
    seen_ts = set()
    unique = []
    for ts, ans in candidates:
        if ts not in seen_ts:
            seen_ts.add(ts)
            unique.append(ans)

    return unique[:NUM_BATCHES]


def grade_all(answer_160: str, questions: list) -> dict:
    """Grade 160-char answer string against question list."""
    batch_scores = []
    total_correct = 0

    for b in range(NUM_BATCHES):
        batch_correct = 0
        for i in range(BATCH_SIZE):
            q_idx = b * BATCH_SIZE + i
            user_letter = answer_160[q_idx]
            correct_letter = questions[q_idx]["ans"]
            if user_letter == correct_letter:
                batch_correct += 1
        batch_scores.append(batch_correct)
        total_correct += batch_correct

    return {"score": total_correct, "total": TOTAL_QUESTIONS, "batch_scores": batch_scores}


def build_result_message(grading: dict, phase_index: int, passed: bool,
                          next_phase: int = None, repeat_weeks: int = None) -> str:
    score = grading["score"]
    total = grading["total"]
    pct = int(score / total * 100)
    batch_scores = grading["batch_scores"]

    batch_line = " | ".join(
        f"Phan {i+1}: {s}/{BATCH_SIZE}" for i, s in enumerate(batch_scores)
    )

    lines = [
        f"KET QUA KIEM TRA — Phase {phase_index}",
        f"Diem: {score}/{total} ({pct}%)",
        batch_line,
        "",
    ]

    if passed:
        lines.append(f"[PASS] Chuc mung! Tien len Phase {next_phase}.")
    else:
        dur = repeat_weeks if repeat_weeks else get_phase_duration_weeks(phase_index)
        needed = PASS_THRESHOLD - score
        lines.append(f"[FAIL] Can on lai. Hoc lai Phase {phase_index} them {dur} tuan.")
        lines.append(f"(Can them {needed} cau dung de dat 120/160)")

    return "\n".join(lines)


def process_task_checkin(state: dict, updates: list) -> dict:
    """
    Look for task completion replies sent after 21:00 today.
    Patterns: ^[\\d\\s]+$ OR ^done$ (case insensitive).
    Returns updated state.
    """
    today = datetime.date.today()
    today_str = str(today)
    tasks_list = get_today_tasks(state)

    if not tasks_list:
        return state

    # Evening reminder is at 21:00 — look for replies from today
    task_pattern = re.compile(r'^[\d\s]+$')
    done_pattern = re.compile(r'^done$', re.IGNORECASE)

    task_reply = None
    latest_ts = 0

    for update in updates:
        msg = update.get("message") or update.get("edited_message")
        if not msg:
            continue
        chat_id = str(msg.get("chat", {}).get("id", ""))
        if chat_id != str(CHAT_ID):
            continue
        text = msg.get("text", "").strip()
        msg_ts = msg.get("date", 0)
        msg_date = datetime.date.fromtimestamp(msg_ts)
        if msg_date != today:
            continue
        if task_pattern.match(text) or done_pattern.match(text):
            if msg_ts > latest_ts:
                latest_ts = msg_ts
                task_reply = text

    if task_reply is None:
        print(f"[GradeQuiz] No task checkin reply found for today.")
        return state

    total = len(tasks_list)
    if done_pattern.match(task_reply):
        completed_indices = list(range(1, total + 1))
        num_done = total
    else:
        parts = task_reply.split()
        completed_indices = []
        for p in parts:
            try:
                idx = int(p)
                if 1 <= idx <= total:
                    completed_indices.append(idx)
            except ValueError:
                pass
        num_done = len(completed_indices)

    state = advance_day(state, completed_indices, tasks_list)
    save_state(state)

    # Preview next day tasks
    from curriculum import CURRICULUM
    phase_idx = state.get("phase_index", 0)
    next_day = state.get("day_index", 0)
    curriculum_days = CURRICULUM.get(phase_idx, [])
    if curriculum_days:
        next_tasks = curriculum_days[next_day % len(curriculum_days)]
        preview = "\n".join(f"  - {t}" for t in next_tasks)
    else:
        preview = "  (khong co nhiem vu)"

    confirm_msg = (
        f"✅ Da ghi nhan {num_done}/{total} nhiem vu hoan thanh.\n"
        f"Ngay mai:\n{preview}"
    )
    send_telegram(confirm_msg)
    print(f"[GradeQuiz] Task checkin: {num_done}/{total} done.")
    return state


def main():
    state = load_state()

    # Always process task checkin regardless of mode
    updates = get_recent_updates(limit=200)
    state = process_task_checkin(state, updates)

    if state["mode"] != "quiz":
        print(f"[GradeQuiz] Mode is '{state['mode']}' — nothing to grade. Exiting.")
        return

    phase_index = state["phase_index"]
    quiz_sent_date = state.get("quiz_sent_date") or str(datetime.date.today())

    from quizzes import QUIZZES
    questions = QUIZZES.get(phase_index)
    if not questions:
        print(f"[GradeQuiz] No quiz for phase {phase_index}. Resetting to study mode.")
        state["mode"] = "study"
        save_state(state)
        return

    # Poll for answers (reuse already-fetched updates)
    batch_answers = collect_batch_answers(updates, quiz_sent_date)
    num_received = len(batch_answers)

    if num_received < NUM_BATCHES:
        msg = (
            f"Moi nhan duoc {num_received}/{NUM_BATCHES} phan tra loi. "
            f"Can du 8 phan moi cham diem."
        )
        print(f"[GradeQuiz] {msg}")
        send_telegram(msg)
        return

    # Concatenate into 160-char string
    answer_160 = "".join(batch_answers)
    print(f"[GradeQuiz] Full answer ({len(answer_160)} chars): {answer_160}")

    grading = grade_all(answer_160, questions)
    score = grading["score"]
    passed = score >= PASS_THRESHOLD

    if passed:
        next_phase = phase_index + 1
        state["phase_index"] = next_phase
        state["phase_start_date"] = str(datetime.date.today())
        state["mode"] = "study"
        state["quiz_sent_date"] = None
        result_msg = build_result_message(grading, phase_index, passed=True, next_phase=next_phase)
    else:
        state["failed_attempts"] = state.get("failed_attempts", 0) + 1
        state["phase_start_date"] = str(datetime.date.today())
        state["mode"] = "study"
        state["quiz_sent_date"] = None
        dur = get_phase_duration_weeks(phase_index)
        result_msg = build_result_message(grading, phase_index, passed=False, repeat_weeks=dur)

    save_state(state)
    ok = send_telegram(result_msg)
    status = "sent" if ok else "FAILED"
    print(f"[GradeQuiz] Result -> Telegram {status}  (score {score}/160, passed={passed})")


if __name__ == "__main__":
    main()

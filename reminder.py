# -*- coding: utf-8 -*-
"""
Dong Y (TCM) Study Reminder — with phase tracking and quiz engine.
Sends Telegram messages for morning (07:00) and evening (21:00) study sessions.
"""

import os
import sys
import time
import requests
import datetime
import random

sys.stdout.reconfigure(encoding='utf-8')

from state import load_state, save_state, is_quiz_time, get_days_in_phase, get_phase_duration_weeks, get_today_tasks

# ── Telegram credentials ──────────────────────────────────────────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8815369190:AAGWX03FTic4lq_J5J8Mqn2xFwE7YhwBxP0")
CHAT_ID   = os.environ.get("CHAT_ID",   "8842938928")

# ── Study phases (0-indexed) ──────────────────────────────────────────────────
PHASES = [
    {
        "name":  "Phase 0 — Nội Kinh Nền Tảng",
        "books": [
            {
                "title": "Hoàng Đế Nội Kinh (Tố Vấn + Linh Khu)",
                "url":   "https://trungtamthuoc.com/bai-viet/sach-hoang-de-noi-kinh-to-van",
                "doc_gi": "Chương Âm Dương, Ngũ Hành, Kinh Lạc",
                "tai_sao": "Khung tần số căn bản — 5 tạng = 5 dải tần",
            },
            {
                "title": "Bát Thập Nhất Nan Kinh",
                "url":   "https://nhattruongkontum.com/download/Sach-Dong-Y/Hoang-de-81-nan-kinh-Bien-Thuoc.html",
                "doc_gi": "Toàn bộ (Nan 1–29 ưu tiên)",
                "tai_sao": "Nan 1–22: mạch học = đọc dao động; Nan 23–29: kinh mạch = đường dẫn Khí",
            },
            {
                "title": "Y Học Tam Tự Kinh",
                "url":   "https://yds.edu.vn/tu-sach-dong-y-y-hoc-tam-tu-kinh-pdf/",
                "doc_gi": "Toàn bộ (ngắn)",
                "tai_sao": "Map nhanh hệ thống, không bỏ bước nào",
            },
            {
                "title": "Nội Kinh nguyên văn Hán",
                "url":   "https://ctext.org/huangdi-neijing/suwen",
                "doc_gi": "Tố Vấn chương 1–9",
                "tai_sao": "Cảm nhận nhịp điệu văn cổ điển, không qua lọc dịch",
            },
        ],
        "focus": "Lý luận âm dương, ngũ hành, tạng phủ, kinh lạc cơ sở.",
    },
    {
        "name":  "Phase 1 — Mạch Học Thực Hành",
        "books": [
            {
                "title": "Mạch Kinh — Vương Thúc Hòa",
                "url":   "https://archive.org/details/wang-pulse-classic",
                "doc_gi": "27 mạch tượng, quyển 1–3",
                "tai_sao": "27 pattern dao động — học bằng TAY, không bằng mắt",
            },
            {
                "title": "Nan Kinh Nan 1–22",
                "url":   "https://ctext.org/nan-jing",
                "doc_gi": "Chỉ phần mạch học",
                "tai_sao": "Cross-check lý luận mạch với Mạch Kinh",
            },
            {
                "title": "Chẩn Mạch Yếu Quyết",
                "url":   "https://nhattruongkontum.com/download/",
                "doc_gi": "Toàn bộ",
                "tai_sao": "Cô đọng hơn Mạch Kinh — dùng để đối chiếu",
            },
        ],
        "focus": "28 loại mạch, cách bắt mạch, phân biệt mạch bệnh lý.",
    },
    {
        "name":  "Phase 2 — Châm Cứu Chuyên Sâu",
        "books": [
            {
                "title": "Châm Cứu Đại Thành Q1",
                "url":   "https://downloadsachmienphi.com/cham-cuu-dai-thanh-quyen-1/",
                "doc_gi": "Huyệt vị 14 kinh chính",
                "tai_sao": "Bách khoa châm cứu — dùng làm reference chính",
            },
            {
                "title": "Châm Cứu Đại Thành Q2",
                "url":   "https://tieudao.info/cham-cuu-dai-thanh-quyen-2.html",
                "doc_gi": "Thủ pháp, phối huyệt lâm sàng",
                "tai_sao": "Kỹ thuật điều chỉnh tần số kích thích qua kim",
            },
            {
                "title": "Hoàng Đế Minh Đường Châm Kinh",
                "url":   "https://nhattruongkontum.com/download/",
                "doc_gi": "Vị trí huyệt gốc + cảm Đắc Khí",
                "tai_sao": "Huyệt vị nguồn gốc cổ nhất — chuẩn hơn các bản sau",
            },
            {
                "title": "Linh Khu — Kinh Lạc",
                "url":   "https://ctext.org/huangdi-neijing/ling-shu-jing",
                "doc_gi": "Chương Kinh Biệt + Kinh Cân",
                "tai_sao": "Hiểu spatial của Khí — mạng lưới dẫn truyền tần số",
            },
        ],
        "focus": "Huyệt vị, thủ pháp châm, cứu pháp, phối huyệt lâm sàng.",
    },
    {
        "name":  "Phase 3 — Thương Hàn & Tạp Bệnh",
        "books": [
            {
                "title": "Thương Hàn Luận",
                "url":   "https://nhattruongkontum.com/download/Sach-Dong-Y/Thuong-Han-Luan-Truong-Trong-Canh-Hoc-Vien-Y-Duoc-Co-Truyen-Viet-Nam.html",
                "doc_gi": "6 kinh biện chứng, đọc nguyên văn + chú giải Thành Vô Kỷ",
                "tai_sao": "6 trạng thái Khí của cơ thể — nền tảng biện chứng",
            },
            {
                "title": "Thương Hàn Luận Q1 — Thái Dương",
                "url":   "https://thuvienpdf.com/thuong-han-luan-quyen-1-thai-duong-kinh",
                "doc_gi": "Toàn bộ Thái Dương kinh",
                "tai_sao": "Thái Dương = cửa ngõ — hiểu đúng trước khi vào 5 kinh còn lại",
            },
            {
                "title": "Tứ Thánh Tâm Nguyên",
                "url":   "https://nhattruongkontum.com/download/",
                "doc_gi": "Phần Dương Khí & Mệnh Môn",
                "tai_sao": "Hoàng Nguyên Ngự tái kiến giải theo Dương Khí — góc nhìn tần số cao",
            },
        ],
        "focus": "Lục kinh biện chứng, phương tễ kinh điển, tạp bệnh nội khoa.",
    },
    {
        "name":  "Phase 4 — Ôn Bệnh Học",
        "books": [
            {
                "title": "Ôn Bệnh Điều Biện",
                "url":   "https://nhattruongkontum.com/download/",
                "doc_gi": "Vệ Khí Dinh Huyết 4 tầng",
                "tai_sao": "4 tầng tần số xâm nhập của ngoại tà — từ ngoài vào trong",
            },
            {
                "title": "Ôn Nhiệt Luận — Diệp Thiên Sĩ",
                "url":   "https://nhattruongkontum.com/download/",
                "doc_gi": "Toàn bộ (ngắn, súc tích)",
                "tai_sao": "Lý luận nhiệt bệnh từ góc Khí hóa — cô đọng nhất phái Ôn Bệnh",
            },
        ],
        "focus": "Vệ khí doanh huyết, tam tiêu biện chứng, bệnh nhiệt ngoại cảm.",
    },
    {
        "name":  "Phase 5 — Tổng Hợp Các Gia",
        "books": [
            {
                "title": "Tỳ Vị Luận — Lý Đông Viên",
                "url":   "https://nhattruongkontum.com/download/",
                "doc_gi": "Toàn bộ",
                "tai_sao": "Trung tiêu = nguồn Khí hậu thiên; người nhạy tần số thường Tỳ Vị nhạy",
            },
            {
                "title": "Đan Khê Tâm Pháp",
                "url":   "https://nhattruongkontum.com/download/",
                "doc_gi": "Âm hư + Khí uất",
                "tai_sao": "Phổ biến ở người nhạy cảm — hiểu để tự điều",
            },
            {
                "title": "Cảnh Nhạc Toàn Thư",
                "url":   "https://nhattruongkontum.com/download/",
                "doc_gi": "Mệnh Môn hỏa + Thận Dương",
                "tai_sao": "Nguồn tần số căn bản của sự sống — tần số thấp 0.1–1Hz",
            },
        ],
        "focus": "Học thuyết tỳ vị, tư âm giáng hoả, bổ mệnh môn — tích hợp toàn diện.",
    },
]

# ── Morning prompts (10 items) ────────────────────────────────────────────────
MORNING_PROMPTS = [
    "Hôm nay hãy đọc chậm, ghi chú từng khái niệm. Kiến thức Đông y thấm qua chiều sâu, không phải tốc độ.",
    "Trước khi học, hít thở sâu 3 lần, ổn định Tâm Khí. Học với tâm thanh tịnh sẽ nhớ lâu hơn.",
    "Hãy liên hệ lý thuyết hôm nay với một triệu chứng thực tế bạn đã gặp hoặc cảm nhận trên cơ thể.",
    "Mỗi ngày một bước nhỏ. Sau 2 năm, bạn sẽ nhìn lại và không ngờ mình đã đi xa đến thế.",
    "Đọc nguyên văn cổ văn, đừng chỉ đọc bản dịch. Cảm nhận nhịp điệu của văn chương y học cổ điển.",
    "Hôm nay hãy thực hành bắt mạch tay trái của chính mình — Thốn, Quan, Xích — trước khi ngồi học.",
    "Tưởng tượng bạn là thầy thuốc đang giải thích cho bệnh nhân. Học để dạy lại — cách nhớ tốt nhất.",
    "Kinh lạc là bản đồ Khí của cơ thể. Hôm nay hãy vẽ lại đường kinh đang học mà không nhìn sách.",
    "Không có bí quyết nào ngoài tính kiên trì. Ngày hôm nay dù bận, hãy đọc ít nhất 2 trang.",
    "Đông y là nghệ thuật quan sát. Hôm nay hãy quan sát màu sắc lưỡi và chất lưỡi của người thân.",
]

# ── Evening review questions (10 items) ──────────────────────────────────────
EVENING_QUESTIONS = [
    "Khí hóa là gì? Phân biệt Nguyên Khí, Tông Khí, Dinh Khí, Vệ Khí — chức năng và nguồn gốc của mỗi loại?",
    "12 kinh chính lưu chú theo thứ tự nào? Tại sao vòng lưu chú bắt đầu từ kinh Phế?",
    "Phân biệt mạch Phù và mạch Hồng. Chúng báo hiệu bệnh gì? Phủ tạng nào liên quan?",
    "Ngũ du huyệt (Tỉnh, Huỳnh, Du, Kinh, Hợp) — ý nghĩa của từng loại và khi nào dùng?",
    "Tam tiêu theo Nội Kinh khác gì với Tam tiêu theo Ôn Bệnh Học? Ảnh hưởng đến châm cứu như thế nào?",
    "Tại sao Thương Hàn Luận nói 'Thái Dương bệnh, mạch Phù, đầu cứng cổ gánh, sợ lạnh'? Giải thích cơ chế.",
    "Phân biệt Chứng Hư và Chứng Thực trong biện chứng lâm sàng. Cho 2 ví dụ cụ thể mỗi loại.",
    "Huyệt Nguyên của 12 kinh có tác dụng đặc biệt gì? Khi nào ưu tiên châm huyệt Nguyên?",
    "Tần số dao động của Khí trong y học cổ truyền liên quan đến fascia/collagen như thế nào theo nghiên cứu hiện đại?",
    "Giải thích cơ chế 'Tỳ thống huyết' và 'Can tàng huyết' — liên hệ lâm sàng với chứng xuất huyết.",
]


# ── Telegram helper ───────────────────────────────────────────────────────────

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


# ── Message builders ──────────────────────────────────────────────────────────

def build_tasks_morning_block(state: dict) -> str:
    tasks = get_today_tasks(state)
    if not tasks:
        return ""
    pending_strings = state.get("_pending_task_strings", [])
    # Split into pending (carried over) and new (the rest)
    pending_count = len(pending_strings)
    new_tasks = tasks[pending_count:]
    pending_tasks = tasks[:pending_count]

    lines = ["\n📋 NHIỆM VỤ HÔM NAY:"]
    for i, t in enumerate(tasks):
        lines.append(f"{i+1}. {t}")

    if pending_tasks:
        lines.append("\n⚠️ Nhắc lại từ hôm qua:")
        for t in pending_tasks:
            lines.append(f"🔁 {t}")

    return "\n".join(lines)


def build_morning_message(phase: dict, state: dict) -> str:
    today_str = datetime.date.today().strftime("%d/%m/%Y")
    tip = random.choice(MORNING_PROMPTS)
    days = get_days_in_phase(state)
    phase_idx = state["phase_index"]
    duration_weeks = get_phase_duration_weeks(phase_idx)

    books_block = ""
    for b in phase["books"]:
        books_block += (
            f'\n<a href="{b["url"]}"><b>{b["title"]}</b></a>\n'
            f'  Đọc gì: {b["doc_gi"]}\n'
            f'  Tại sao: {b["tai_sao"]}\n'
        )

    tasks_block = build_tasks_morning_block(state)

    msg = (
        f"[ĐÔNG Y — BUỔI SÁNG]  {today_str}\n"
        f"------------------------\n\n"
        f"<b>{phase['name']}</b>\n"
        f"Ngày {days+1} / {duration_weeks*7} ({duration_weeks} tuần)\n\n"
        f"<b>Lộ trình hôm nay:</b>{books_block}\n"
        f"<b>Trọng tâm:</b> {phase['focus']}\n\n"
        f"{tasks_block}\n\n"
        f"<b>Tip:</b>\n{tip}\n\n"
        f"Chúc buổi học sâu và an tĩnh!"
    )
    return msg


def build_tasks_evening_block(state: dict) -> str:
    tasks = get_today_tasks(state)
    if not tasks:
        return ""
    lines = ["✅ ĐIỂM DANH NHIỆM VỤ HÔM NAY:"]
    for i, t in enumerate(tasks):
        lines.append(f"{i+1}. {t}")
    lines.append("")
    lines.append("→ Reply số thứ tự đã hoàn thành (VD: 1 2 3 hoặc 1 3)")
    lines.append("→ Nếu xong hết reply: done")
    return "\n".join(lines)


def build_evening_message(phase: dict, state: dict) -> str:
    today_str = datetime.date.today().strftime("%d/%m/%Y")
    question = random.choice(EVENING_QUESTIONS)
    days = get_days_in_phase(state)
    phase_idx = state["phase_index"]
    duration_weeks = get_phase_duration_weeks(phase_idx)

    tasks_block = build_tasks_evening_block(state)

    msg = (
        f"[ĐÔNG Y — ÔN TẬP BUỔI TỐI]  {today_str}\n"
        f"------------------------\n\n"
        f"<b>{phase['name']}</b>\n"
        f"Ngày {days+1} / {duration_weeks*7}\n\n"
        f"<b>Câu hỏi ôn tập:</b>\n{question}\n\n"
        f"{tasks_block}\n\n"
        f"Nhắc nhở: Trước khi ngủ, thực hành bắt mạch 5 phút.\n"
        f"Quan sát: nhịp, lực, độ sâu, hình thái.\n\n"
        f"Kiên trì mỗi ngày — Đại Y sẽ đến!"
    )
    return msg


def send_quiz(phase_index: int):
    import datetime as dt
    from quizzes import QUIZZES
    questions = QUIZZES.get(phase_index)
    if not questions:
        print(f"[ERROR] No quiz found for phase {phase_index}")
        return

    BATCH_SIZE = 10
    NUM_BATCHES = 16  # 160 / 10

    for batch_num in range(1, NUM_BATCHES + 1):
        start = (batch_num - 1) * BATCH_SIZE
        end = start + BATCH_SIZE
        batch = questions[start:end]

        lines = [f"KIỂM TRA PHASE {phase_index} — Phần {batch_num}/16", ""]

        for i, q in enumerate(batch):
            cau_num = start + i + 1
            lines.append(f"Câu {cau_num}: {q['q']}")
            for letter, opt_text in q["opts"].items():
                lines.append(f"{letter}) {opt_text}")
            lines.append("")

        lines.append("-> Trả lời: gửi 10 chữ cái liên tiếp (VD: ABCDABCDAB)")

        msg = "\n".join(lines)
        ok = send_telegram(msg)
        status = "sent" if ok else "FAILED"
        print(f"[DongY] Quiz Phase {phase_index} Phan {batch_num}/16 -> Telegram {status}")

        time.sleep(3)

    send_telegram(
        f"Đã gửi 16 phần đề thi (160 câu). "
        f"Trả lời từng phần bằng 10 chữ cái. "
        f"Pass: 120/160 (75%)."
    )

    # Update state
    state = load_state()
    state["mode"] = "quiz"
    state["quiz_sent_date"] = str(dt.date.today())
    state["quiz_phase"] = phase_index
    save_state(state)


def send_morning_reminder(state: dict):
    phase_idx = state["phase_index"]
    phase = PHASES[min(phase_idx, len(PHASES) - 1)]
    message = build_morning_message(phase, state)
    ok = send_telegram(message)
    status = "sent" if ok else "FAILED"
    print(f"[DongY] Morning reminder Phase {phase_idx} -> Telegram {status}")


def send_evening_reminder(state: dict):
    phase_idx = state["phase_index"]
    phase = PHASES[min(phase_idx, len(PHASES) - 1)]
    message = build_evening_message(phase, state)
    ok = send_telegram(message)
    status = "sent" if ok else "FAILED"
    print(f"[DongY] Evening reminder Phase {phase_idx} -> Telegram {status}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    import datetime as dt
    state = load_state()

    # Determine session: check SESSION env var first, then fall back to hour detection
    session_env = os.environ.get("SESSION")
    if session_env == "morning":
        session = "morning"
    elif session_env == "evening":
        session = "evening"
    else:
        now_hour = dt.datetime.now().hour
        if 6 <= now_hour <= 8:
            session = "morning"
        elif 20 <= now_hour <= 22:
            session = "evening"
        else:
            # Test/manual run outside scheduled hours
            session = "morning"
            print(f"[DongY] Manual run at hour {now_hour} — defaulting to morning reminder")

    if is_quiz_time(state) and state["mode"] == "study":
        # Send quiz (send_quiz updates state internally)
        # On GitHub Actions, state write inside send_quiz is allowed (quiz mode transition)
        send_quiz(state["phase_index"])
    elif state["mode"] == "study":
        # Normal study reminder
        if session == "morning":
            send_morning_reminder(state)
            save_state(state)
        else:
            send_evening_reminder(state)
            save_state(state)
    else:
        # mode == "quiz" — waiting for user response, grade_quiz.py handles this
        print(f"[DongY] Mode is '{state['mode']}' — waiting for quiz answer. Run grade_quiz.py at 21:30.")


if __name__ == "__main__":
    main()

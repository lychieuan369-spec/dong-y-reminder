# -*- coding: utf-8 -*-
import os
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz

ICT = pytz.timezone('Asia/Ho_Chi_Minh')

def run_morning():
    os.environ['SESSION'] = 'morning'
    import importlib, reminder
    importlib.reload(reminder)
    reminder.main()

def run_evening():
    os.environ['SESSION'] = 'evening'
    import importlib, reminder
    importlib.reload(reminder)
    reminder.main()

def run_grade():
    import importlib, grade_quiz
    importlib.reload(grade_quiz)
    grade_quiz.main()

scheduler = BlockingScheduler(timezone=ICT)
scheduler.add_job(run_morning, CronTrigger(hour=7, minute=0, timezone=ICT))
scheduler.add_job(run_evening, CronTrigger(hour=21, minute=0, timezone=ICT))
scheduler.add_job(run_grade,   CronTrigger(hour=21, minute=30, timezone=ICT))

print("Scheduler started. Jobs: 7h, 21h, 21h30 ICT")
scheduler.start()

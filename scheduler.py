# -*- coding: utf-8 -*-
import os
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

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

scheduler = BlockingScheduler(timezone='UTC')
# All times explicit UTC — 7h ICT = 0h UTC, 21h ICT = 14h UTC
scheduler.add_job(run_morning, CronTrigger(hour=0,  minute=0,  timezone='UTC'))
scheduler.add_job(run_evening, CronTrigger(hour=14, minute=0,  timezone='UTC'))
scheduler.add_job(run_grade,   CronTrigger(hour=14, minute=30, timezone='UTC'))

print("Scheduler started (UTC). Morning=0h, Evening=14h, Grade=14h30")
scheduler.start()

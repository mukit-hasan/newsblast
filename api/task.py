from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from api.sendmail import send_schedule_email


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_schedule_email, 'interval', seconds=60)
    scheduler.start()

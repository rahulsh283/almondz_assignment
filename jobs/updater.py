from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_user_data_and_upload_s3_csv


def start():
    # change the time in hour minutes or second when you want to run this database cleaningjob
    csv_upload_trigger = CronTrigger(
        year="*", month="*", day_of_week="0", hour="00", minute="00", second="00"
    )

    scheduler = BackgroundScheduler()
    scheduler.add_job(get_user_data_and_upload_s3_csv, trigger=csv_upload_trigger)
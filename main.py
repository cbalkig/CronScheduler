from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time


class CronDate:
    def __init__(self, _text):
        _text = _text.replace("?", "*")
        data = _text.split(" ")
        data.reverse()

        if len(data) < 7:
            raise Exception("Missing parameter in cron text")

        self.year = data[0]
        self.month = data[1]
        self.day = data[2]
        self.day_of_week = data[3]
        self.hours = data[4]
        self.minutes = data[5]
        self.seconds = data[6]


def my_func():
    print('Hi {time}'.format(time=datetime.now()))


if __name__ == '__main__':
    cron_text = '0 0/1 * 1/1 * ? *'
    cron_data = CronDate(cron_text)

    scheduler = BackgroundScheduler()
    scheduler.add_job(my_func, trigger='cron', year=cron_data.year, day_of_week=cron_data.day_of_week,
                      month=cron_data.month, day=cron_data.day, hour=cron_data.hours, minute=cron_data.minutes,
                      second=cron_data.seconds)
    scheduler.start()

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

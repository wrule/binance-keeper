#!/opt/homebrew/bin/python3

import time
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(timezone = 'UTC')

def hello():
  print('你好，世界')

scheduler.add_job(hello, 'interval', seconds = 1)
scheduler.start()

while True:
  time.sleep(1)

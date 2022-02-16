#!/opt/homebrew/bin/python3

import time
import yaml
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(timezone = 'UTC')

def hello():
  print('你好，世界')

scheduler.add_job(hello, 'cron', second = 58)
scheduler.start()

print(yaml.safe_load(open('.secret.yaml', 'r')))

while True:
  time.sleep(1)

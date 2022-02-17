#!/opt/homebrew/bin/python3

import time
import yaml
from apscheduler.schedulers.background import BackgroundScheduler
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

scheduler = BackgroundScheduler(timezone = 'UTC')

def hello():
  print('你好，世界')

scheduler.add_job(hello, 'cron', second = 58)
scheduler.start()

secret = yaml.safe_load(open('.secret.yaml', 'r'))

client = Client(secret['APIKEY'], secret['APISECRET'])
time_res = client.get_server_time()

# print(time_res)
depth = client.get_order_book(symbol='BTCUSDT')
# print(depth)
# for key in depth.keys():
#   print(key)
# info = client.get_symbol_info('BNBBTC')
# print(info)

# avg_price = client.get_avg_price(symbol='BTCUSDT')
# print(avg_price)

trades = client.get_recent_trades(symbol='BNBBTC')
print(trades);

while True:
  time.sleep(1)

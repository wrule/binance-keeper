#!/opt/homebrew/bin/python3

import time
import yaml
from apscheduler.schedulers.background import BackgroundScheduler
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

def main():
  symbol = 'BTCUSDT'
  secret = yaml.safe_load(open('.secret.yaml', 'r'))
  print('你好，世界')

if __name__ == '__main__':
  main()

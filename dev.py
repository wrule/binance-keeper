#!/opt/homebrew/bin/python3
import time
from src.spot.kline.watcher import KLineWatcher

watcher = KLineWatcher('BTCUSDT', '1m', 3)
watcher.Start()
time.sleep(20)
watcher.Stop()

# import time
# from binance.websocket.spot.websocket_client import SpotWebsocketClient as WSClient
# from binance.spot import Spot as Client
# from datetime import datetime

# class K:
#   def __init__(self, data):
#     self.time = data[0] / 1e3
#     self.open = float(data[1])
#     self.high = float(data[2])
#     self.low = float(data[3])
#     self.close = float(data[4])
#     self.volume = float(data[5])
#   time = 0
#   open = 0
#   close = 0
#   high = 0
#   low = 0
#   volume = 0


# spot_client = Client('https://testnet.binance.vision')
# klines = spot_client.klines('BTCUSDT', '1d', limit = 10)
# for row in klines:
#   k = K(row)
#   print(datetime.fromtimestamp(k.time), k.close)
# print(len(klines))


# def message_handler(data):
#   if 'k' in data.keys():
#     print(data['k'])

# my_client = WSClient('wss://testnet.binance.vision')
# my_client.start()

# my_client.kline(
#   symbol = 'btcusdt',
#   id = 1,
#   interval = '1m',
#   callback = message_handler,
# )

# time.sleep(3000)

# my_client.stop()




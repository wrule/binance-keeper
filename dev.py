#!/opt/homebrew/bin/python3

import time
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WSClient
from binance.spot import Spot as Client
from datetime import datetime

spot_client = Client('https://testnet.binance.vision')
klines = spot_client.klines('BTCUSDT', '1d', limit = 100)
for row in klines:
  print(datetime.fromtimestamp(row[0] / 1e3), row[4])
print(len(klines))


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

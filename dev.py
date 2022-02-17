#!/opt/homebrew/bin/python3

import time
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

def message_handler(data):
  if 'k' in data.keys():
    print(data['k'])

my_client = Client('wss://testnet.binance.vision')
my_client.start()

my_client.kline(
  symbol = 'btcusdt',
  id = 1,
  interval = '1m',
  callback = message_handler,
)

time.sleep(3000)

my_client.stop()

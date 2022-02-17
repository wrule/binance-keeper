#!/opt/homebrew/bin/python3

import time
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

def message_handler(data):
  if 'c' in data.keys():
    print(data['c'])

my_client = Client()
my_client.start()

my_client.mini_ticker(
    symbol="btcusdt",
    id=2,
    callback=message_handler,
)

time.sleep(3000)

my_client.stop()

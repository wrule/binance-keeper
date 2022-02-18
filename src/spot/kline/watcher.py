from binance.spot import Spot as SpotClient
from binance.websocket.spot.websocket_client import SpotWebsocketClient
from src.k import CreateByWS, Create

class KLineWatcher:
  def __init__(
    self,
    symbol: str,
    interval: str,
    limit: int,
  ):
    self.symbol = symbol
    self.interval = interval
    self.limit = limit
    self.client = SpotClient('https://testnet.binance.vision')
    self.wsClient = SpotWebsocketClient('wss://testnet.binance.vision')

  symbol: str = 'BTCUSDT'
  interval: str = '1d'
  limit: int = 100
  client: SpotClient
  wsClient: SpotWebsocketClient
  
  def wsData(self, data):
    if 'e' in data.keys():
      k = CreateByWS(data['k'])
      print(k.close, k.closed)

  def Start(self):
    print('开始监听')
    klines = self.client.klines(self.symbol, self.interval, limit = self.limit)
    # k = Create(klines[len(klines) - 2])
    # print(klines)
    self.wsClient.start()
    self.wsClient.kline(
      symbol = self.symbol,
      id = 1,
      interval = self.interval,
      callback = self.wsData,
    )

  def Stop(self):
    print('结束监听')
    self.wsClient.stop()

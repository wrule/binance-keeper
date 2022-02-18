from binance.spot import Spot as SpotClient
from binance.websocket.spot.websocket_client import SpotWebsocketClient
from src.k import K, CreateByWS, Create, CreateKLines
from typing import Dict, List, Any

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
  
  KLines: List[K]
  wsK: K
  
  def wsData(self, data):
    if 'e' in data.keys():
      self.K = CreateByWS(data['k'])

  def Start(self):
    print('开始监听')
    self.KLines = CreateKLines(self.client.klines(self.symbol, self.interval, limit = self.limit))
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

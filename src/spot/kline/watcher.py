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
  
  KLines: List[K] = None
  wsK: K = None
  
  def doSomething(self):
    times = [item.time for item in self.KLines]
    index = times.index(self.wsK.time) if self.wsK.time in times else -1
    if index < 0:
      self.KLines.append(self.wsK)
      print('不存在')
    else:
      self.KLines[index] = self.wsK
      print('存在')
    
  
  def wsData(self, data):
    if 'e' in data.keys():
      # oldK = self.wsK
      self.wsK = CreateByWS(data['k'])
      self.doSomething()
      # if not oldK is None:
      #   if oldK.time != self.wsK.time:
      #     self.updateKLines()

  def updateKLines(self):
    self.KLines = CreateKLines(self.client.klines(self.symbol, self.interval, limit = self.limit))

  def Start(self):
    print('开始监听')
    self.updateKLines()
    self.wsClient.kline(
      symbol = self.symbol,
      id = 1,
      interval = self.interval,
      callback = self.wsData,
    )
    self.wsClient.start()

  def Stop(self):
    print('结束监听')
    self.wsClient.stop()

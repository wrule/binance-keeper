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
  wsKLine: K = None
  
  def KLinesClosed(self):
    return list(filter(lambda kline: kline.closed, self.KLines))
  
  def action(
    self,
    closedKLines: List[K],
    lastKLine: K,
    allKLines: List[K],
  ):
    print('最新价格', lastKLine.close)
  
  def tryToAction(self):
    KLinesLen = len(self.KLines)
    if self.KLines is None or KLinesLen < 1:
      return
    if self.wsKLine is None:
      return
    lastIndex = KLinesLen - 1
    lastKLine = self.KLines[lastIndex]
    if self.wsKLine.time == lastKLine.time:
      self.KLines[lastIndex] = self.wsKLine
      self.action(self.KLinesClosed(), lastKLine, self.KLines)
    elif self.wsKLine.time > lastKLine.time:
      self.updateKLines()
  
  def wsData(self, data):
    if 'e' in data.keys():
      self.wsKLine = CreateByWS(data['k'])
      self.tryToAction()

  def updateKLines(self):
    self.KLines = CreateKLines(self.client.klines(self.symbol, self.interval, limit = self.limit))
    self.tryToAction()

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

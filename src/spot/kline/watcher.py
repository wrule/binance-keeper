
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

  symbol: str = 'BTCUSDT'
  interval: str = '1d'
  limit: int = 100

  def Start(self):
    print('开始监听')

  def Stop(self):
    print('结束监听')

from typing import Dict, List, Any

class K:
  def __init__(
    self,
    time: int,
    open: float,
    close: float,
    high: float,
    low: float,
    volume: float,
    closed: bool,
  ):
    self.time = time,
    self.open = open
    self.close = close
    self.high = high
    self.low = low
    self.volume = volume
    self.closed = closed
  time: int
  open: float
  close: float
  high: float
  low: float
  volume: float
  closed: bool

def Create(list: List[Any]):
  return K(
    list[0],
    float(list[1]),
    float(list[4]),
    float(list[2]),
    float(list[3]),
    float(list[5]),
    True,
  )

def CreateKLines(list: List[List[Any]]):
  result = [Create(item) for item in list]
  if len(result) > 0:
    result[len(result) - 1].closed = False
  return result
  
def CreateByWS(data: Dict[str, Any]):
  return K(
    data['t'],
    float(data['o']),
    float(data['c']),
    float(data['h']),
    float(data['l']),
    float(data['v']),
    data['x'],
  )

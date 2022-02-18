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
  ):
    self.time = time,
    self.open = open
    self.close = close
    self.high = high
    self.low = low
    self.volume = volume
  time: int
  open: float
  close: float
  high: float
  low: float
  volume: float

def Create(list: List[Any]):
  return K(
    list[0],
    float(list[1]),
    float(list[4]),
    float(list[2]),
    float(list[3]),
    float(list[5]),
  )
  
def CreateByWS(data: Dict[str, Any]):
  return K(
    data['t'],
    float(data['o']),
    float(data['c']),
    float(data['h']),
    float(data['l']),
    float(data['v']),
  )

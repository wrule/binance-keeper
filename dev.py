#!/opt/homebrew/bin/python3
import time
from src.spot.kline.watcher import KLineWatcher

watcher = KLineWatcher('BTCUSDT', '1d', 100)
watcher.Start()
time.sleep(200)
watcher.Stop()

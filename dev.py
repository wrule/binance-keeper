#!/opt/homebrew/bin/python3
import time
from src.spot.kline.watcher import KLineWatcher

watcher = KLineWatcher('LINKUSDT', '1d', 100)
watcher.Start()
time.sleep(60)
watcher.Stop()

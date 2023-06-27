import os
import psutil
import time

p = psutil.Process(os.getpid())
target = 20 # target CPU usage in percentage
interval = 0.1 # interval to check and adjust CPU usage
sleeptime = 0.01 # initial sleep time between work cycles

while True:
    start = time.time()
    # do some work
    for i in range(100000):
        x = i ** 2
    end = time.time()
    worktime = end - start
    # check and adjust CPU usage
    usage = p.cpu_percent(interval=interval)
    if usage < target:
        sleeptime -= 0.001
    elif usage > target:
        sleeptime += 0.001
    # prevent sleep time from going negative
    if sleeptime < 0:
        sleeptime = 0
    # sleep for some time
    time.sleep(sleeptime)

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:11:05 2019

@author: lenovo
"""

import time

print("Press ENTER to begin.Afterwards, \npress ENTER to click the stopwatch. \nPress Ctrl-C to quit")
input() #press ENTER to begin
print('Started')
startTime = time.time() #get the first lap's start time
lastTime = startTime
lapNum = 1

# start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() #reset last lap time
except KeyboardInterrupt:
    print('\n Done')
        
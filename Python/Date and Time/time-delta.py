#!/bin/usr/python3
import datetime
testcase = int(input())
for i in range(testcase):
    time1 = input().strip()
    time2 = input().strip()
    timeformat = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.datetime.strptime(time1, timeformat)
    t2 = datetime.datetime.strptime(time2, timeformat)
    print(int(abs(t1 - t2).total_seconds()))


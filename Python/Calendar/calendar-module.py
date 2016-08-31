#!/bin/usr/python3
import calendar
month, date, year = map(int, input().split())
print(calendar.day_name[calendar.weekday(year, month, date)].upper())

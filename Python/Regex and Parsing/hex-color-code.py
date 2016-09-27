#!/usr/local/bin/python3
import re

for i in range(int(input())):
    match = re.findall(r"(?<= |:)((?:#)(?:[0-9A-Fa-f]{1,2}){3,4})", input())
    if match:
        for i in match:
            print (i)

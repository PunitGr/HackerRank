#!/usr/local/bin/python3
import re
string = input()
find = input()
m = re.finditer(r'(?=(' + find + '))', string)
match = False

for x in m:
    match = True
    print ((x.start(1), x.end(1) - 1))

if match == False:
    print ((-1, -1))


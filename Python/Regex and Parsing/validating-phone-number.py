#!/usr/local/bin/python3
import re
n = int(input())
for _ in range(n):
    if re.match("^[7-9]{1}?[0-9]{9}$", input()):
        print("YES")
    else:
        print("NO")

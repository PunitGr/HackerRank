#!/usr/local/bin/python3
import re
for _ in range(int(input())):
    email = input()
    match = re.match(r'.*?\<([a-z]+[a-z0-9_\.\-]+)@([a-z]+)\.([a-z]{1,3})\>.*?', email)
    if match is not None and len(match.groups())==3:
        print(email)

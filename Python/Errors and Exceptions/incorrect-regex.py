#!/usr/bin/python

import re
for _ in range(int(input())):
    try:
        re.compile(input())
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)

#!/usr/local/bin/python3
import re
for _ in range(int(input())):
    print(bool(re.match("^[-+]?[0-9]*\.[0-9]+$", input())))

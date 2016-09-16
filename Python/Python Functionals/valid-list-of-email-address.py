#!/usr/local/bin/python3
import re

valid = list()
for email in [ input() for i in range(int(input())) ]:
    if re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", email):
        valid.append(email)
valid.sort()
print (valid)


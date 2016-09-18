#!/usr/local/bin/python3
import re
l = re.search(r'([A-Za-z0-9])\1+', input())
if l is None:
    print ('-1')
else:
    print (l.group(0)[0])

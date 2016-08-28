#!/bin/python3
from collections import deque
d = deque()
for i in range(int(input())):
    op = input().split()
    getattr(d,op[0])(*map(int, op[1:]))
print(' '.join(map(str, d)))

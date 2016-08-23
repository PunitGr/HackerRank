#!/bin/python3
from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)

for i in range(n):
    d[input()].append(i + 1)
for i in range(m):
    x = input()
    if x in d:
        print(' '.join(map(str, d[x])))
    else:
        print('-1')

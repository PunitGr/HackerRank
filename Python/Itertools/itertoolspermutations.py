#!/bin/python3
from itertools import permutations
s,n = input().split()
for x in permutations(sorted(s), int(n)):
    print(''.join(x))

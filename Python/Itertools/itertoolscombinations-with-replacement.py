#!/bin/python3
from itertools import combinations_with_replacement
s,n = input().split()
for e in combinations_with_replacement(sorted(s), int(n)): 
    print(''.join(e))

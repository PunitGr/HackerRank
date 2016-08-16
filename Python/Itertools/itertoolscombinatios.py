#!/bin/python3
from itertools import combinations
s,n = input().split()
for i in range(1,int(n)+1):
	for e in combinations(sorted(s),i): print(''.join(e))

#!/bin/python3
from itertools import product
(k, m) = map(int, input().split())
l = list()
for i in range(k):
    lis = list(map(int, input().split()))
    n = lis[0]
    l.append(lis[1:])
    assert len(l[i]) == n

sum_max = 0
for i in product(*l):
    total = sum([x*x for x in i]) % m
    
    if total > sum_max:
        sum_max = total
print(sum_max)

#!/bin/usr/python3
from collections import OrderedDict
n = int(input())
l = OrderedDict()
for i in range(n):
    word = input()
    if word in l:
        l[word] += 1
    else:
        l[word] = 1
print(len(l))
for i in l:
    print(l[i], end = " ")

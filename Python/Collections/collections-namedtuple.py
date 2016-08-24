#!/bin/usr/python3
from collections import namedtuple
n = int(input())
x = namedtuple("Student", input().strip().split())
avg = 0
for i in range(n): avg += float(x(*input().strip().split()).MARKS)
print (avg / n)

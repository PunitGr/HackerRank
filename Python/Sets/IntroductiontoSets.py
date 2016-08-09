#!/bin/python3
n = int(input())
h = list(map(int, input().split()))
assert len(h) == n
h = set(h)
print (float(sum(h) / len(h)))

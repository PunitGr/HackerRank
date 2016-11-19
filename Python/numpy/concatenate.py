#!/usr/local/bin/python3
import numpy
n, m, p = map(int, input().split())
print(numpy.array([input().split() for _ in range(n+m)], int))


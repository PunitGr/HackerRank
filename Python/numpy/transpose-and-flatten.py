#!/usr/local/bin/python3
import numpy

n,m = map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)

print(numpy.transpose(array))
print(array.flatten())


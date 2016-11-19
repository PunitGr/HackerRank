#!/usr/local/bin/python3
import numpy
n = int(input())
array1 = numpy.array([input().split() for _ in range(n)], int)
array2 = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(array1, array2))


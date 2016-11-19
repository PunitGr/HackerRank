#!/usr/local/bin/python3
import numpy
n, m = map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)
print(numpy.mean(array, axis=1), numpy.var(array, axis=0),numpy.std(array, axis=None), sep='\n')


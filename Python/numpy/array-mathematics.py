#!/usr/local/bin/python3
import numpy
n, m = map(int, input().split())
array1, array2 = (numpy.array([input().split() for _ in range(n)], int) for x in range(2))
print(array1 + array2, array1 - array2, array1 * array2, array1 // array2, array1 % array2, array1 ** array2, sep='\n')


#!/usr/local/bin/python3
import numpy
array = numpy.array(input().split(), float)
print(numpy.floor(array), numpy.ceil(array), numpy.rint(array), sep='\n')


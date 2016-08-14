#!/bin/python3
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(' '.join(str(e) for e in product(A, B)))

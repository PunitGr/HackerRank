#!/bin/python3

from collections import Counter
input()
print(Counter(map(int, input().split())).most_common()[-1][0])


#!/bin/usr/python3
from collections import Counter

count = Counter(input().strip())
i = 0
for v, k in sorted((-v, k) for k, v in count.most_common()):
	print (k + ' ' + str(-v))
	i += 1
	if i >= 3: break

#!/bin/usr/python3
from collections import deque

T = int(input())

for i in range(T):
    n = int(input())
    sideLengths = deque(map(int, input().split()))

    lastLength = max(sideLengths)
    answer = 'Yes'

    while len(sideLengths) > 0:
        if len(sideLengths) == 1:
            item = sideLengths.pop()
        else:
            if sideLengths[0] < sideLengths[-1]:
                item = sideLengths.pop()
            else:
                item = sideLengths.popleft()

        if item > lastLength:
            answer = 'No'
            break
        else:
            lastLength = item

    print (answer)

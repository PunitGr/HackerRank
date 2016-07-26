#!/bin/python3

import sys
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.sort(reverse=True)
while len(arr) > 0:
    print (len(arr))
    block_cut = arr.pop()
    while len(arr) > 0 and arr[-1] <= block_cut:
        arr.pop()


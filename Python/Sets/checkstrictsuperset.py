#!/bin/python3
A = set(map(int, input().split()))
n = int(input())
Flag = True
for i in range(n):
    B = set(map(int, input().split()))
    if B.issubset(A) == False:
        Flag = False
    elif len(B) >= len(A):
        Flag = False
print (Flag)

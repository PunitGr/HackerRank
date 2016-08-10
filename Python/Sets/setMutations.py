#!/bin/python3

l = int(input())
A = set(map(int, input().split()))
n = int(input())

for x in range(n):
    (operation, length) = input().split()
    S = set(map(int, input().split()))

    if operation == 'intersection_update':
        A.intersection_update(S)
    elif operation == 'update':
        A.update(S)
    elif operation == 'symmetric_difference_update':
        A.symmetric_difference_update(S)
    elif operation == 'difference_update':
        A.difference_update(S)
    else:
        assert False

print (sum(A))

#!/usr/local/bin/python3
N, M = map(int, input().split())

A = [[int(x) for x in input().split()] for e in range(N)]
K = int(input())
for i in sorted(A, key=lambda i:i[K]):
    print(' '.join(map(str, i)))


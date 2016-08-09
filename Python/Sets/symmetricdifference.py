#!/bin/python3
M = int(input())
S1 = list(map(int, input().split()))
assert len(S1) == M
S1 = set(S1)

N = int(input())
S2 = list(map(int, input().split()))
assert len(S2) == N
S2 = set(S2)

u = S1.difference(S2)
v = S2.difference(S1)
w = set()
w = u.union(v)

wlist = list(w)
wlist.sort()
for i in range(len(wlist)):
    print (wlist[i])

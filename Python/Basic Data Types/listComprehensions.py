#!/bin/python3
x = int(input())
y = int(input())
z = int(input())
N = int(input())
print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if sum([a,b,c])!=N])

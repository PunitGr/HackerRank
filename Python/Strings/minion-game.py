#!/bin/python3
S = input()
n = len(S)
stuart = 0
kevin = 0
for i in range(n):
    if S[i] in ['A', 'E', 'I', 'O', 'U']:
        kevin += n - i
    else:
        stuart += n - i

if stuart > kevin:
    print "Stuart", stuart
elif stuart < kevin:
    print "Kevin", kevin
else:
    print "Draw"


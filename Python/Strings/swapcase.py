#!/bin/python3
# change case of string
S = list(input())
for i in range(len(S)):
    if S[i].isupper() == True:
        S[i] = S[i].lower()
    else:
        S[i] = S[i].upper()
print (''.join(S))

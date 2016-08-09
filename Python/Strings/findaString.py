#!/bin/python3
# to find a substring in the input string
s1 = input()
s2 = input()
count = 0
for i in range(len(s1)):
    if s1[i:].startswith(s2):
        count += 1
print (count)

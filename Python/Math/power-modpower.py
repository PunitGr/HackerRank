#!/usr/bin/python
a = int(input())
b = int(input())
m = int(input())
power = 1
result = 0

for i in range(0,b):
    power = power * a
print (power)
result = power % m
print (result)
    

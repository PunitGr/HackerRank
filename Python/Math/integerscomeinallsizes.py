#!/usr/bin/python
a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = 0
power1 = 1
power2 = 1
for i in range(0,b):
    power1 = long(power1 * a)
    
for i in range(0,d):
    power2 = long(power2 * c)
    
result = long(power1 + power2)
print (result)

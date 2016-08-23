#!/bin/python3
from collections import Counter
x = int(input())
sizes = Counter(map(int, input().split()))
n = int(input())
money = 0
for i in range(n):
    shoe_size, price = map(int, input().split())
    if sizes[shoe_size] > 0:
        sizes[shoe_size] = sizes[shoe_size] - 1
        money = money + price
print(money)


#!/usr/local/bin/python3
n = int(input())
series = list()
for i in range(n):
    series.append(i if i < 2 else series[i - 2] + series[i - 1])
print(list(map(lambda cube: cube ** 3, series)))

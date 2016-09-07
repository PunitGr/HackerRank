#!/usr/local/bin/python3
N, X = map(int, input().split())

subjects = list()

for i in range(X):
    subjects.append(list(map(float, input().split())))

students = list(zip(*subjects))

average = []
for i in range(N):
    average.append(sum(students[i])/X)
    print (average[i])


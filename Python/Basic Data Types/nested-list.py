# find the second max scorer in the nested list
#!/bin/python3
N = int(input())

myList = list()
for i in range(0, N):
    myList.append([input(), float(input())])

scores = set(myList[x][1] for x in range(0, N))
scores = list(scores)
scores.sort()

students = list()
for i in range(0, N):
    if scores[1] == myList[i][1]:
        students.append(myList[i][0])
        students = list(students)

students.sort()
for x in students:
    print (x)

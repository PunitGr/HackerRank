import re
n, m = map(int, input().split())

col = list()
for i in range(m):
    col.append(list())

for i in range(n):
    row = input()
    for j in range(m):
        col[j].append(row[j])

string = str()
for c in col:
    string += ''.join(c)

print(re.sub(r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])',' ', ''.join(string)))


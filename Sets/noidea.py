n, m = map(int, input().split())
i=[int(u) for u in input().split()]
A={int(u) for u in input().split()}
B={int(u) for u in input().split()}

x = 0
for j in i:
    x = x + (j in A) - (j in B)
print (x)

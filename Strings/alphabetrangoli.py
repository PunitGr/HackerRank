import string

n = int(input())
x = 2 * n - 1
s = string.ascii_lowercase[:n][::-1]

for j in range(x):
    i = min(j, x - j - 1)
    print('-' * (x - 2 * i - 1) + '-'.join(list(s[:i] + s[i] + s[:i][::-1])) + '-' * (x - 2 * i - 1))

from itertools import combinations
N = int(input())
L = input().split()
K = int(input())
numerator = 0
denominator = 0
for e in combinations(L,K):
    numerator +='a' in e[:K]
    denominator += 1
print(numerator * 1.0 / denominator)

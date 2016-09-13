#!/usr/local/bin/python3
n = int(input())
numbers = list(map(int, input().split()))
print (all(int(num) > 0 for num in numbers) and any(str(nums)[::-1] == str(nums) for nums in numbers))

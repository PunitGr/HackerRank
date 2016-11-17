#!/usr/local/bin/python3
def format(phoneNumber):
    def number(l):
        phoneNumber(["+91 " + c[-10:-5] + " " + c[-5:]for c in l])
    return number

@format
def sortedNumber(lis):
    print(*sorted(lis), sep='\n')

lis = [input() for _ in range(int(input()))]

sortedNumber(lis)

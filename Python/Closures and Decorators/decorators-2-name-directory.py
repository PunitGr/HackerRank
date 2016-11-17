#!/usr/local/bin/python3
import operator

person = [input().split() for _ in range(int(input()))]

def personList(obj):
    def inner(person):
        return[obj(i) for i in sorted(person, key=operator.itemgetter(2))]
    return inner

@personList
def format(person):
    return ("Mr. " if person[-1] == "M" else "Ms. ") + " ".join(person[:-2])

print(*format(person), sep='\n')

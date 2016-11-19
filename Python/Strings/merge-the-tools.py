#!/usr/local/bin/python3
string, num = input(), int(input()) 
for i in zip(*[iter(string)] * num):
    dictionary = dict()
    print(''.join([ dictionary.setdefault(x, x) for x in i if x not in dictionary ]))

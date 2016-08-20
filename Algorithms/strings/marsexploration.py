#!/bin/python3
print(len([1 for x,y in zip(input(),'SOS'*33) if x is not y]))

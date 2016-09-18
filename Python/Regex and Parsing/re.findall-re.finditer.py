#!/usr/local/bin/python3
import re
consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
vowels = "AEIOUaeiou"
x = re.findall(r'(?<=[' + consonants + '])[' + vowels + ']{2,}(?=[' + consonants + '])', input())
if x:
    for i in x: print(i)
else: print('-1')

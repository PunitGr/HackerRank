#!/bin/usr/python3
import re
from collections  import OrderedDict
n = int(input())
dictionary = OrderedDict()
for i in range(n):
    l = re.split(r'(\d+)$',input().strip())
    item_name = l[0]
    item_price = int(l[1])
    if item_name not in dictionary:
        dictionary[item_name] = int(item_price)
    else:
        dictionary[item_name] = dictionary[item_name] + item_price
        
for i in dictionary:
    print( i + str(dictionary[i]))

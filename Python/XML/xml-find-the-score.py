#!/usr/local/bin/python3
import xml.etree.ElementTree as etree
n = int(input())
lis = ''
count = 0
for i in range(n):
    lis += input()

tree = etree.fromstring(lis)
for i in tree.iter():
    count += len(i.attrib)
print(count)


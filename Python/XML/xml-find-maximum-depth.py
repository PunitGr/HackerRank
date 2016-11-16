#!/usr/local/bin/python3
import xml.etree.ElementTree as etree
xml = ''
for _ in range(int(input())):
    xml += input()
tree = etree.ElementTree(etree.fromstring(xml))
def depth(root):
    return(1 + max([0] + [depth(child) for child in root])) 
print(depth(tree.getroot()) - 1)


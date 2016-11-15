#!/usr/local/bin/python3
import re
for _ in range(int(input())):
    validity = "Invalid"
    cardnumber = input().strip()
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$', cardnumber)
    if pre_match:
        string = ''.join(pre_match.group(0).split('-'))
        match = re.search(r'(\d)\1{3,}', string)
        if match:
            print('Invalid') 
        else:
            print('Valid')
    else:
        print('Invalid')

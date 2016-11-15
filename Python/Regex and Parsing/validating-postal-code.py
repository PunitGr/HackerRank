#!/usr/local/bin/python3
import re 
postal_code = input().strip() 
print(bool(re.search(r'^[1-9]\d{5}$', postal_code) and len(re.findall(r'(?=(\d)\d\1)', postal_code)) < 2))

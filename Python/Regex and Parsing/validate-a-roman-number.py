#!/usr/local/bin/python3
import re
roman = input()
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
if re.search(pattern, roman):
    print(True)
else: print(False)

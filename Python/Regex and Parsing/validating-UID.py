#!/usr/local/bin/python3
import re
for i in range(int(input())):
    UID = input()
    validity = "Invalid"
    if len(UID) == 10:
        count = 0
        match = re.findall(r'(?:([0-9A-Za-z])(?!.*\1))', UID)
        for x in match:
            count += 1
        if count == 10:
            if re.search(r'(.*[0-9]+.*[0-9]+.*[0-9]+.*)', UID) != None:
                if re.search(r'(.*[A-Za-z]+.*[A-Za-z]+.*)', UID) != None:
                    validity = "Valid"
    print(validity)

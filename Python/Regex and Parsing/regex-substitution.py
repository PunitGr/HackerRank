#!/usr/local/bin/python3
import re
for _ in range(int(input())):
	print(re.sub(r"(?<= )\|\|(?= )", "or", re.sub(r"(?<= )&&(?= )", "and", input())))


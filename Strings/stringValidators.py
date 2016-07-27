S = input()
for x in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']: print(any(getattr(y,x)() for y in S))

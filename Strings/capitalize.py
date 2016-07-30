string = input()

print(' '.join(e[0].upper() + e[1:].lower() if e else '' for e in string.split(' ')))

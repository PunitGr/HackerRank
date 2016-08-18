from itertools import groupby
S = str(input())
print (' '.join('(' + str(len(list(string[1]))) + ', ' +str(string[0]) + ')' for string in groupby(S.strip())))

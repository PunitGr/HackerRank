#designer door mat problem
# Size: 7 x 21 
#    ---------.|.---------
#    ------.|..|..|.------
#    ---.|..|..|..|..|.---
#    -------WELCOME-------
#    ---.|..|..|..|..|.---
#    ------.|..|..|.------
#    ---------.|.---------

N, M = map(int,input().split())
a = [('.|.'*i).center(M,'-') for i in range(1,N,2)]
for e in a+['WELCOME'.center(M,'-')] + list(reversed(a)): print(e)

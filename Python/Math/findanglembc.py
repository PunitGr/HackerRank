# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, acos, degrees
AB = int(raw_input())
BC = int(raw_input())
AC = sqrt((AB * AB) + (BC * BC))
AM = AC / 2.0
print str(int(round(degrees(acos((BC/2.0)/AM))))) + "°"


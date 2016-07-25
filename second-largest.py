# find second max number in a list
def SecondMax(myList, length):
    if myList[length-1] == myList[length-2]:
        SecondMax(myList, length-1)
    else:
        print (myList[length-2])

N = int(input())
x = input()
a1 = x.split()
mylist = list(map(int, a1)) 
mylist.sort()
length = len(mylist)
SecondMax(mylist, length)

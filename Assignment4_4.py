#4.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even.
# Map function will calculate its square. Reduce will return addition of all  that numbers.
#Input List = [5,2,3,4,3,4,1,2,8,10]
#List after filter = [2,4,4,2,8,10]
#List after map = [4,16,16,4,64,100]
#Output of reduce = 204



from functools import *

a=[]
n=int(input("enter no.of elements: "))
for i in range(n):
    el=int(input("enter element: "))
    a.append(el)
print('Input List',a)


c = list(filter(lambda no:(no%2==0), a))
print("List after filter: ",c)
m = list(map(lambda no: (no**2),c))
print("List after map: ",m)
r =reduce(lambda no1,no2: (no1 + no2),m)
print("Output of reduce: ",r)
print()

#****************************************************


import functools  

a=[]
n=int(input("enter no.of elements: "))
for i in range(n):
    el=int(input("enter element: "))
    a.append(el)
print('Input List',a)


c = list(filter(lambda no:(no%2==0), a))
print("List after filter: ",c)
m = list(map(lambda no: (no**2),c))
print("List after map: ",m)
r =functools.reduce(lambda no1,no2: (no1 + no2),m)
print("Output of reduce: ",r)
print()

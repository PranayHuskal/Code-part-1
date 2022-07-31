#3.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or 
#equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all 
#that numbers.
#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000


from functools import *

a=[]
n=int(input("enter no.of elements: "))
for i in range(n):
    el=int(input("enter element: "))
    a.append(el)
print('Input List',a)


c = list(filter(lambda no:(no >=70), a))
f= list(filter(lambda no: (no<=90),c))
print("List after filter: ",f)
m = list(map(lambda no: (no + 10),f))
print("List after map: ",m)
r =reduce(lambda no1,no2: (no1 * no2),m)
print("Output of reduce: ",r)
print()

##*************************************************

import functools 

a=[]
n=int(input("enter no.of elements: "))
for i in range(n):
    el=int(input("enter element: "))
    a.append(el)
print(a)


c = list(filter(lambda no:(no >=70), a))
f= list(filter(lambda no: (no<=90),c))
print("Filtere(): ",f)
m = list(map(lambda no: (no + 10),f))
print("map(): ",m)
r =functools.reduce(lambda no1,no2: (no1 * no2),m)
print("reduce(): ",r)


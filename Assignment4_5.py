#5.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all prime numbers.
# Map function will multiply each number by 2. Reduce will return maximum number from that numbers.
# (also use normal function instead of lambda function)
#Input List = [2,70,11,10,17,23,31,77]
#List after filter = [2,11,17,23,31]
#List after map = [4,22,34,46,62]
#Output of reduce = 62



import functools
 
def chkprime(a):
    lst = []
    for i in a:
        ch=0
        for j in range(2,i):
            if i%j==0:
                ch=1
                break
        if ch==0:
            lst.append(i)
    return lst

def multi(a):
    mult= list(map(lambda n:n*2,a))
    return mult


def main():

    a=[]
    n=int(input("enter no.of elements: "))
    for i in range(n):
        el=int(input("enter element: "))
        a.append(el)
    print('Input List',a)
    
    b = chkprime(a)
    print("list after filter: ",b)
    
    c= multi(b)
    print("List after map:",c)
    
    d=max(c)
    print("List after reduce:",d)
 
if __name__ == "__main__":
    main()

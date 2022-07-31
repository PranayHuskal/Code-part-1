#1.Write a program which contains one lambda function which accepts one parameter and return
#power of two.
#Input : 4 Output : 16
#SInput : 6 Output : 36


def show(n):
    a=(lambda x:x**2)
    print(a(n))
    
def main():    
    n=int(input("Enter a number: "))
    show(n)

if __name__ == '__main__':
    main()
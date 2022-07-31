#1.Write a program which contains one lambda function which accepts one parameter and return
#power of two.
#Input : 4  4 Output : 16
#Input : 6  3 Output : 18

def mult(a,b):
    l=lambda x,y: x*y
    print(l(a,b))

def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    mult(a,b)


if __name__ == '__main__':
    main()
    
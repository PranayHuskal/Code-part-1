#1. Write a recursive program which display below pattern.
#  input:   5
#  output:  *  *  *  *  *
def star(no):
    i=0
    if(i<no):
        print('*',end= ' ')
        star(no-1)
        
def main():
    value=int(input("Enter a number:"))
    star(value)

if __name__ =="__main__":
    main()

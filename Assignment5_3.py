#3. Write a recursive program which display below pattern.
#  input:   5
#  output:  5  4  3  2  1  


def show(no):
    i=1 
    if(i<=no):
        print(no, end = ' ')
        no=no-1
        show(no)

def main():
    n=int(input('enter a number: '))
    show(n)

if __name__ == "__main__":
    main()
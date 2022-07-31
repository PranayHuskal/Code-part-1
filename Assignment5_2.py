#2. Write a recursive program which display below pattern.
#  input:   5
#  output:  1  2  3  4  5

i=1
def show(no):
    global i 
    if(i<=no):
        print(i, end = ' ')
        i=i+1
        show(no)

def main():
    n=int(input('enter a number: '))
    show(n)

if __name__ == "__main__":
    main()
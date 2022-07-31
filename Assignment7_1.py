#1.Write a program which contains one class named as BookStore.
#BookStore class contains two instance variables as Name ,Author.
#That class contains one class variable as NoOfBooks which is initialise to 0.
#There is one instance methods of class as Display which displays name , Author and number of books.
#Initialise instance variable in init method by accepting the values from user as name and author.
#Inside init method increment value of NoOfBooks by one.
#After creating the class create the two objects of BookStore class as

#Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
#Obj1.Display()                                    # Linux System Programming by Robert Love. No of books : 1

#Obj2 = BookStore(“C Programming”, “Dennis Ritchie”)
#Obj2.Display()                             # C Programming by Dennis Ritchie. No of books : 2

class BookStore:
    NoofBooks=0
    def __init__(self,n,a):
        self.name=n
        self.author=a
        BookStore.NoofBooks += 1       
        
    
    def Display(self):
       
        print("Name Book:",self.name,"Book Author:",self.author,"No of Books:",BookStore.NoofBooks)
        
        print()
        
    
    
    
def main():
    n=input('Enter the name of book: ')
    a=input("Enter the author: ")
    
    Obj1=BookStore(n,a)
    Obj1.Display()
    
    
    n=input('Enter the name of book: ')
    a=input("Enter the author: ")
    
    Obj2=BookStore(n,a)
    Obj2.Display()
    
    
    
if __name__=="__main__":
    main()
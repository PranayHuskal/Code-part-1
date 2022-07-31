# 1.Write a program which contains one class named as Demo. Demo class contains two instance variables as no1 ,no2.
# That class contains one class variable as Value. There are two instance methods of class as Fun and Gun which displays values of instance
# variables. Initialise instance variable in init method by accepting the values from user. After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:
    value=10
    def __init__(self,x,y):
        self.no1=x
        self.no2=y
    
    def Fun(self):
        return self.no1,self.no2
        
    def Gun(self):
        return self.no1,self.no2
        
        
def main(): 
    v1=int(input("Enter first number:"))
    v2=int(input("Enter second number:"))
    v3=int(input("Enter third number:"))
    v4=int(input("Enter fourth number:"))

    Obj1=Demo(v1,v2)
    Obj2=Demo(v3,v4)

    r1=Obj1.Fun()
    print(r1)

    r2=Obj2.Fun()
    print(r2)

    r3=Obj1.Gun()
    print(r3)

    r4=Obj2.Gun()
    print(r4)
    
if __name__ =="__main__":
    main()
#Q3. Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Value1 ,Value2. Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user. Addition() method will perform addition of Value1 ,Value2 and return result.
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
# Division() method will perform division of Value1 ,Value2 and return result.
# After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.value2=0
        
    def Accept(self):
        self.Value1=int(input('Enter the number:'))
        self.Value2=int(input('Enter the number:'))
        
    def Addition(self):
        return(self.Value1+self.Value2)
                
    def Substraction(self):
        return(self.Value1-self.Value2)
        
    def Multiplication(self):
        return(self.Value1*self.Value2)
        
    def Division(self):
        return(self.Value1/self.Value2)
        
def main():

    x=Arithmetic()
    x.Accept()

    ret=x.Addition()
    print("Addition is:",ret)

    ret1=x.Substraction()
    print('Substraction is:',ret1)

    ret2=x.Multiplication()
    print('Multiplication is:',ret2)

    ret3=x.Division()
    print('Division is :',ret3)

if __name__=="__main__":
    main()
       
    
    
#Q3. Write a program which contains one class named as Numbers. Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.SumFactors() method will return addition of all factors. 
# Use this method in any another method as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
    def __init__(self,value):
        self.value=value
        
    def ChkPrime(self,no):
        for i in range(2,no):
            if no%i==0:
                return False
                break
        else:
            return True
    
    def Factor(self,no):
        for i in range(1,int(no/2)+1):
            if (no%i)==0:
                print(i,end=' ')
     
    def ChkPerfect(self,no):
        sum=0
        for i in range(1,int(no/2)+1):
            if no%i == 0:
                sum = sum + i
        if sum == no:
            return True
        else:
            return False
            
    def SumFactors(self,no):
        Add = 0
        for i in range(1,int(no/2)+1):
            if (no%i) == 0:
                Add = Add + i
        return Add
        
def main():
    no=int(input('Enter number: '))
    obj =Arithmetic(no)
    
    Ret = obj.ChkPrime(no)
    if Ret == True:
        print(no,'is prime number')
    else:
        print(no,'is not prime number')
    
    obj.Factor(no)
    print()
    
    Ret = obj.ChkPerfect(no)
    if Ret == True:
        print(no,' is Perfect Number')
    else:
        print(no,' is not Perfect Number')
    
    Ret = obj.SumFactors(no)
    print("Addition of ",no,"'s factor is",Ret)
    
if __name__ == "__main__":
    main()

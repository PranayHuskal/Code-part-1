#Q.2. Write a program which contains one class named as BankAccount.BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.Inside init method initialise all name and amount variables by accepting
# the values from user.There are Four instance methods inside class as Display(), Deposit(), Withdraw(),CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
    ROI=10.5
    def __init__(self):
        self.name= " "
        self.amount= 0
        self.withdraw=0
        
        
    def Deposit(self):
        self.name= input('Enter your name: ')
        self.amount=int(input('Enter amount to deposit: '))
        self.year = int(input('no.of year to calculate interest: ' ))
        self.withdraw= int(input('Enter the amount to withdraw: '))
    
    def Display(self):
        print('Your name is :',self.name)
        print('Remaining balance in your account is : ',self.amount)       
    
    def Withdraw(self):
        accbalance= self.amount - self.withdraw
        print('Your reamining Account Balance is:',accbalance)
        
    def CalculateIntrest(self):
        Intrest = (self.amount * self.year * BankAccount.ROI)/100
        print('Intrest for',self.year,'year is :',Intrest)
     

    
    
def main():
    obj1 = BankAccount()
    
    obj1.Deposit()
    obj1.Display()
    obj1.CalculateIntrest()   
    obj1.Withdraw()



if __name__ == "__main__":
    main()
   
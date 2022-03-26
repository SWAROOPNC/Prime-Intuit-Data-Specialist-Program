

#Python program to demonstrate private members
# Creating a Base class
class Base:
    def __init__(self):
        self.a = 'Prime Intuit'
        self.__c = 'Prime Intuit_Private'

    def display(self):
        print(self.__c)


# Creating a derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.a)
 #       print(self.__c)

# Calling constructor of
# Base class

# Driver code
obj1 = Base()
obj1.display()
obj2 = Derived()
obj2.display()


class parent:
    def __init__(self):
        self.a = 10
    def display(self):
        print(self.a)

class child(parent):
    def __init__(self):
        parent.__init__(self)
        print(self.a)
        self.c = 20


def result(self):
    print(self.c)


obj = parent()
obj.display()
b = obj.a
print(b)
obj.a = b + 5
print(obj.a)


## Try everything using a bank example

class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello ! Welcome to your bank ")

    def opening_account(self):
        name = input("Enter Acoount holder name: ")
        age = int(input("Enter Age : "))
        pan_num = input("Enter Pan Number: ")
        print("Account opened sucessfully : ", name, " ", age, " ", pan_num)

    def deposit(self):
        amount = float(input("Enter the deposit amount: "))
        self.balance += amount
        print("You have deposited : ", amount)

    def withdrawal(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def balance1(self):
        print("Available Balance is : ", self.balance)

    def loan(self):
        loan_amt = int(input("Enter amount Required: "))
        if (loan_amt < self.balance * 10):
            print("You are eligable for the loan : ", "AnnualInterest rate would be 10%")
        else:
            print("You are not eligable for this loan amount, Try a lesser amount")


Jayanagar = Bank_Account()
Jayanagar.opening_account()
Jayanagar.deposit()
Jayanagar.balance += 200
Jayanagar.balance1()
Jayanagar.loan()


# inheritance
class JP_Nagar(Bank_Account):
  def __init__(self, fd_amount, years):
    self.balance = 0
    self.fd_interest = .06
    self.fd_amount = fd_amount
    self.years = years
  def fd_output(self):
    print("Maturity amount = ", (self.fd_amount + self.fd_amount * self.fd_interest * self.years))
JPN = JP_Nagar(1000, 3)
JPN.fd_output()
JPN.deposit()
JPN.balance1()


# polymorphism

class personal_loan(Bank_Account):
  def loan(self):
    print("You are eligable for personal loan amount, 5 times your balance @ 12% interest")

pl = personal_loan()
pl.loan()

"""
l1 = [1,2,3]
l2 = ['a', 'b', 'c']

print(str(l1))
print(' '.join(str(l1)))

print(str(l2))
print(' '.join(l2))


y = " Now is the perfect time to do the right thing"
z = "-----------Join this to center------------"""
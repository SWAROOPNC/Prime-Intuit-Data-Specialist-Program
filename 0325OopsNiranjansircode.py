#add __
class customer():
    def _init_(self, name, id, type, acc_num,address, pan):
        self.cust_name = name
        self.cust_id = id
        self.acc_type = type
        self.acc_num = acc_num
        self.cust_address = address
        self.cust_pan = pan
        self.cust_balance = 0
    def display(self):
        print(self.cust_name, self.acc_num, self.acc_type)
        print('\n', self.cust_balance)
    def deposit(self, amt):
        self.cust_balance = self.cust_balance + amt
        print("you have deposited Rs: ", amt)
        print('\n', 'Your current balance = ', self.cust_balance)
    def withdraw(self, amt):
        if amt>self.cust_balance:
            print("You do not have enough balance, please try lower amount")
        else:
            print("you have withdrawn : ", amt)
            self.cust_balance = self.cust_balance - amt
            print("Balance after withdrawl: ", self.cust_balance)






Niranjan = customer('Niranjan.K',1203445, 'Savings', '016901520808', 'JP Nagar', 'ALPKF1203')
Niranjan.display()

Guru = customer('Guru Prasad', 1238763, "Savings", '01690134567878','JP Nagar','ALGHE2333')
Guru.display()

class customer_IB(customer):
    def _init_(self, IPF, ATO, TR,name, id, type, acc_num,address, pan):
        customer._init_(self, name, id, type, acc_num,address, pan)
        self.IPF = IPF
        self.ATO = ATO
        self.TR = TR
    def display_1(self):
        print(self.cust_name, self.acc_num, self.acc_type)
        print('\n', self.cust_balance)
        print(self.IPF, self.TR, '\n', self.ATO)

Niri = customer_IB('4cr', '5cr', '30Lac', 'Niranjan.K',1203445, 'Savings', '016901520808', 'JP Nagar', 'ALPKF1203')
print('\n'"**************************")
Niri.display_1()
print('\n'"**************************")
print(Niri.display())

Niri.deposit(500)
Niri.withdraw(200)
Niri.display_1()
Guru.deposit(1000)
Guru.withdraw(500)
Guru.display()

#Python program to demonstrate private members
# Creating a Base class
class Base:
    def _init_(self):
        self.a = 'Prime Intuit'
        self.__c = 'Prime Intuit_Private'

    def display(self):
        print(self.__c)


# Creating a derived class
class Derived(Base):
    def _init_(self):
        Base._init_(self)
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
    def init(self):
        self.a = 10

    def display(self):
        print(self.a)


class child(parent):
    parent._init_(self)
    def _init_(self):
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
    def init(self):
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
  def init(self, fd_amount, years):
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

'''
l1 = [1,2,3]
l2 = ['a', 'b', 'c']

print(str(l1))
print(' '.join(str(l1)))

print(str(l2))
print(' '.join(l2))


y = " Now is the perfect time to do the right thing"
z = "-----------Join this to center------------"

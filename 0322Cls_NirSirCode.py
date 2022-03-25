class customer():
    def __init__(self, name, id, type, acc_num,address, pan): #note __ double underscore
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
    def withdraw(self,amt):
        if amt > self.cust_balance :
            print("You dont have sufficient balance , try lower amount")
        else :
            print("you have witdrawn ",amt)
            self.cust_balance = self.cust_balance -amt
            print("Balance after withdrawl",self.cust_balance)

Niranjan = customer('Niranjan.K',1203445, 'Savings', '016901520808', 'JP Nagar', 'ALPKF1203')
Niranjan.display()

Guru = customer('Guru Prasad', 1238763, "Savings", '01690134567878','JP Nagar','ALGHE2333')
Guru.display()
Niranjan.deposit(500)
Niranjan.withdraw(200)
Guru.deposit(1000)
Niranjan.display()
Guru.display()
class customer_IB(customer):
    def __init__(self, IPF, ATO, TR,name, id, type, acc_num,address, pan):
        customer.__init__(self, name, id, type, acc_num,address, pan)
        self.IPF = IPF
        self.ATO = ATO
        self.TR = TR
    def display_1(self):
        print(self.cust_name, self.acc_num, self.acc_type)
        print('\n', self.cust_balance)
        print(self.IPF, self.TR, '\n', self.ATO)

Niranjan = customer_IB('4cr', '5cr', '30Lac', 'Niranjan.K',1203445, 'Savings', '016901520808', 'JP Nagar', 'ALPKF1203')
print('\n'"**************************")
Niranjan.display_1()
print('\n'"**************************")
print(Niranjan.display())

"""uncommenting """
# Python program to
# demonstrate private members
print('\n'"**************************")
# Creating a Base class
class Base:
    def __init__(self):
        self.a = 'Prime Intuit'
        self.__c = 'Prime Intuit_Private'

    def display(self):
        print(self.a)
        print(self.__c)


# Creating a derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.a)
        #print(self.__c) #this if not commented will throw erroe for obj2 derived ,

# Calling constructor of
# Base class
print("&&&&&&&&&&&&&&&&&&&&&&&")
# Driver code
print("&&&&&&&&&&&&&&&&&&&&&&&")
obj1 = Base()
print("++++++++++++++++++++++++")
obj1.display()
print("&&&&&&&&&&&&&&&&&&&&&&&")
obj2 = Derived() #in this c throws error , like child accesing parent locker
print("++++++++++++++++++++++++")
#AttributeError: 'Derived' object has no attribute '_Derived__c'
#calling display from base class , this works ,
obj2.display() #in display can be  prints
# like child accesing parent locker using authorisatin letter , or ATM
#AttributeError: 'Derived' object has no attribute '_Derived__c'
#pvt variable ex balance can only be altered by amethod like withdraw and deposit
#polymorphism
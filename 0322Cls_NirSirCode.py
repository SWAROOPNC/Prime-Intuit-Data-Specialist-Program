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

# Python program to
# demonstrate private members

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
#        print(self.__c)

# Calling constructor of
# Base class

# Driver code
obj1 = Base()
obj1.display()
obj2 = Derived()
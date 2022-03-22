#class
class customer :
    #constructor
    def __init__(self,name,id,type,acc_num, address , pan ):
        self.cust_name = name
        self.cust_id = id
        self.acc_type = type
        self.acc_num = acc_num
        self.cust_address = address
        self.cust_pan = pan
        self.cus_balance = 0
    def display(self):
        print(self.cust_name , self.acc_num,self.acc_type,"\n",self.cus_balance,self.cust_address)
    def deposit(self,amt):
        self.cus_balance = self.cus_balance + amt
        print("You have deposited Rs. ",amt)
        print("\nyour new balance ",self.cus_balance)

Niranjan = customer("Niranjan",120344,"Savings","0169213783","JP Nagar","GCxps1752l")
print(Niranjan.acc_num)
print(Niranjan.cus_balance)
Niranjan.display()

Swaroop = customer("Swaroop N C",123456,"Savings",64021036390,"Gubbi","GCXPS1752l")
Swaroop.display()
Niranjan.deposit(500)

#Inheritence
class customer_IB(customer):
    def __init__(self,IPF, ATO, TR,name, id, type,acc_num , address , pan):
        customer.__init__(self,name, id, type,acc_num , address , pan)
        """self.name = name1
        self.address = address1
        self.pan = pan1"""
        self.IPF = IPF
        self.ATO = ATO
        self.TR = TR
    def display1(self):
        print(self.cust_name , self.acc_num , self.cust_pan)
        print("\n",self.cus_balance)
        print(self.IPF , self.ATO , self.TR)
#ND1 =
ND = customer_IB("4Cr","10L","10L","ND","##","SB","640210","GBB","AMZ")
print("***************")
ND.display1()
print("***************")
ND.display()
print("***************")

#inherting just few attributes from private class

class Base :
    def __init__(self):
        self.a="PI"
        self.__c = "PI Private"
    def display2(self):
        print(self.__c)
#derived class
class Derived(Base) :
    def __init__(self):
        Base.__init__(self)
        print("calling private member of base class")
        print(self.a)
        #print(self.__c) wont work
obj1 = Base()
obj1.display2()
obj2 = Derived()
obj2.display2()

# class
class customer :
    #constructor
    def __init__(self,name,id,type,acc_num, address , pan , balance):
        self.cust_name = name
        self.cust_id = id
        self.acc_type = type
        self.acc_num = acc_num
        self.cust_address = address
        self.cust_pan = pan
        self.cus_balance = balance
    def display(self):
        print(self.cust_name , self.acc_num,self.acc_type,"\n",self.cus_balance,self.cust_address)


Niranjan = customer("Niranjan",120344,"Savings","0169213783","JP Nagar","GCxps1752l",0)
print(Niranjan.acc_num)
print(Niranjan.cus_balance)
Niranjan.display()

Swaroop = customer("Swaroop N C",123456,"Savings",64021036390,"Gubbi","GCXPS1752l",360)
Swaroop.display()
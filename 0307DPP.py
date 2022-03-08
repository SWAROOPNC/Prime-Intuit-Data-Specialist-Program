#Todays DPP: Take a list as input and find if the second highest value is a prime number or not

#Take List input
lus = []
len = int(input("Enter number of elements in list : ")) # number of elements as input
for i in range(0, len): # iterating till the range
    lus.append(int(input(" enter individual elements ")))  # adding the element
print("Unsorted list",lus)

#To Find 2nd highest
ls=sorted(lus)
print("sorted list",ls)
sechigh=ls[len-2]
print("second highest num is ",sechigh)

#Program to check prime number
indicator = True
x= sechigh
for i in range (2,x-1) :
    if (x%i == 0 ) :
        indicator = False
    elif(x==1) :
        indicator = True
if (indicator == True ) :
    print(" Sec High is prime ")
else :
    print (" Sec High is not prime")
    
"""Alternate way"""
a=[]
len=int(input("enter the length of list:"))
for i  in range(0,len):
    y=int(input("enter the elements of the list:"))
    a.append(y)
print(a)
b=max(a)
print(b)
a.remove(b)
print(a)
c=max(a)

indicator = True
x= c
for i in range (2,x-1) :
    if (x%i == 0 ) :
        indicator = False
    elif(x==1) :
        indicator = True
if (indicator == True ) :
    print(" NUm is prime ")
else :
    print (" Num is not prime")
    

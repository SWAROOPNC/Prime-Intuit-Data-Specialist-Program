#sechighUsingMaxMethod
# divide and check 

#Take List input
lus = []
len = int(input("Enter number of elements in list : ")) # number of elements as input
for i in range(0, len): # iterating till the range
    lus.append(int(input(" enter individual elements ")))  # adding the element
print("Unsorted list",lus)

#To Find 2nd highest using Max
#To remove 1st max 

maxn = lus[0]
for i in lus : 
    if (i>maxn ) : 
        maxn = i 
print("lus ",lus)
print("maxn ",maxn)
print("lus.remove(max)",lus.remove(maxn))
#To get 2nd max 
maxn = lus[0]

for i in lus : 
    if (i>maxn ) : 
        maxn = i 
print("lus ",lus)
print("maxn ",maxn)

#Program to check prime number
indicator = True
x= maxn
for i in range (2,x-1) :
    if (x%i == 0 ) :
        indicator = False
    elif(x==1) :
        indicator = True
if (indicator == True ) :
    print(" Sec High is prime ")
else :
    print (" Sec High is not prime")
    
    
#similarly sir told we can do like this using min method , where we compare 2 #uccessibe elements and append to 
#new list then can get last -2 number 
# but i coudnt get it , though i tried it didnt worked 
"""
#Sec high using min method 

#Take List input
lus = []
len = int(input("Enter number of elements in list : ")) # number of elements as input
for i in range(0, len): # iterating till the range
    lus.append(int(input(" enter individual elements ")))  # adding the element
print("Unsorted list",lus)
lnew = []

#To Find 2nd highest using minimum method 
#To remove 1st max 

#To get 2nd max 
minn=lus[0]
print("minn=lus[0]",minn)
for i in lus : 
    print("i",i)
    print("i<minn",i<minn)
    if (i<minn) : 
        lnew.append(i)
        print("lnew",lnew)
        i=minn
        print("i/minn",minn)
        
    
    

print("lus ",lus)
print("lnew ",lnew)

#Program to check prime number
indicator = True
x= lnew[-2]
for i in range (2,x-1) :
    if (x%i == 0 ) :
        indicator = False
    elif(x==1) :
        indicator = True
if (indicator == True ) :
    print(" Sec High is prime ")
else :
    print (" Sec High is not prime")
"""

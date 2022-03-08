
# USe of break , to break lopop , or control shifted after loop
l2 = [2,4,6,8,10]
print(l2)

for i in l2 :
    print(len(l2))
    print(i)
    if (i>5) :
        break
print(" im out of loop1")

#print list using enumerTE

for i in enumerate(l2) :
    print(i)
print(" im out of loop2")

# continue , to ignore rest of loop statement , move control back to loop , not broke the loop , to skip 1 or more iteration
for i in l2 :
    if (i==6) :
        continue
    print(i)
print(" im out of loop3")

for i in l2 :
    if (i==6) :
        continue
        print(i)
print(" im out of loop4")

# pass statement , statements fter pass is
for i in l2 :
    if (i<10) :
        print(i)
    else :
        pass
"""Continue vs pass, they do completely different things. pass simply does nothing, while continue goes on with the next loop iteration. 
In your example, the difference would become apparent
 if you added another statement after the if: 
 After executing pass, this further statement would be executed. After continue, it wouldn't."""
print(" im out of loop5")
for i in l2 :
    if (i<10) :
        print(i)
    else :
        pass
        print("22222")
print(" im out of loop6")
for i in l2 :
    if (i<8) :
        print(i)
    else :
        continue
        print("22222")
print(" im out of loop6")
#observe diff bw pass & continue

# in a given list , how identify if contain even number , if contain even 1 even print list contains even number

l5=[1,3,5,7,8,9,11]
indicator = False
for i in l5 :
    if (i%2 == 0 ) :
        indicator = True
        break
if ( indicator == True ) :
    print(" List  contains even number")
else :
    print(" List NOT contains even num")

#taking list as input and same program way1
l6 = []
len = int(input("Enter number of elements in list : ")) # number of elements as input
for i in range(0, len): # iterating till the range
    l6_i = int(input(" enter individual elements "))
    l6.append(l6_i)  # adding the element
print(l6)
indicator = False
for i in l6 :
    if (i%2 == 0 ) :
        indicator = True
        break
if ( indicator == True ) :
    print(" List  contains even number")
else :
    print(" List NOT contains even num")

#taking list as input and same program way2
l6 = []
len = int(input("Enter number of elements in list : ")) # number of elements as input
for i in range(0, len): # iterating till the range
    l6.append(int(input(" enter individual elements ")))  # adding the element
print(l6)
indicator = False
for i in l6 :
    if (i%2 == 0 ) :
        indicator = True
        break
if ( indicator == True ) :
    print(" List  contains even number")
else :
    print(" List NOT contains even num")

#check if a number is prime
indicator = True
x= int(input(" enter a number to check prime "))
for i in range (2,x-1) :
    if (x%i == 0 ) :
        indicator = False
    elif(x==1) :
        indicator = True
if (indicator == True ) :
    print(" NUm is prime ")
else :
    print (" Num is not prime")

#check if list is prime

ind = True
l5 =[]
len = int(input("Enter the length of the list : "))
for x in range(0, len):
    y = int(input("Eneter element of the list :"))
    l5.append(y)
print(l5)

for i in l5:
    if (i == 1):
        ind = True
    else:
        for y in range(2, i): #y=2,3,4......
            ind = True
            if (i % y == 0):
                ind = False
                break
    if (ind == True):
        print("List contains a prime number")
        break
if ind == False:
    print("List does not contain a prime number")
    
#check if list is prime
#instead of lisr number rangle say 10-20 , print within range , can take range for first for loop DPP
l5 =[]
len = int(input("Enter the length of the list : "))
for x in range(0, len):
    y = int(input("Eneter element of the list :"))
    l5.append(y)
print(l5)
initial = int(input("Enter Initial index value of range to check "))
last = int(input("Enter last index value of range to check "))
ind = True
for i in range(initial,last+1):
    z=l5[i]
    print("i ",i)
    print("z = l5[i] ",z)
    if (z == 1):
        ind = True
    else:
        for y in range(2, z): #y=2,3,4......
            print("y ",y)
            ind = True
            if (z % y == 0):
                print("i%y",(i%y))
                ind = False
                break
    if (ind == True):
        print("specified range in List contains a prime number")
        break
if ind == False:
    print("specified range in List does not contain a prime number")

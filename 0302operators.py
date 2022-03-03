#Comparision 2 numbers Operator
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))

print(a>b)

if(a>b) :
    print(" A is greater than B", a)
else :
    print("B is less than A" , b )

#Comparision 3 numbers Operator

a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number "))
c = int(input("Enter 3rd number "))

#using nested if
if (a>b):
    if (a>c) :
        print ("A is great")
    else :
        print("C is great")
else :
    if (b>c):
            print(" B is great")
    else :
        print("C is great")
#using and operator
if (a > (b and c)):
    print("A is greater")
elif (b > (a and c)):
    print("B is greater")
else:
    print("C is greater")
#using elif
if (a > b):
    if (a > c):
        print("A is greatest")
elif (b > a):
    if (b > c):
        print("B is greatest")
    else:
        print("C is greatest")
#oddeven
a = int(input("Enter number "))
if (a%2==1) :
    print("Number is odd",a)
else :
    print("number is even",a)
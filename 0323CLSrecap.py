#find max of 3 number
a = int (input("Enter num 1 "))
b = int (input("Enter num 2 "))
c = int (input("Enter num 3 "))

if (a>(b and c)) :
        print(a,"is greater than ",b , c)
elif(b>(a and c)) :
        print(b,"is greater than ",a , c)
else :
    print(c,"is greater than ",a,b)
#alternate way
if (a> b) :
    if(a>c) :
        print(a,"is greater than ",b , c)
elif(b>c) :
        print(b,"is greater than ",a , c)
else :
    print(c,"is greater than ",a,b)
print("**************************************************")
#take 3 sides as input and check if right angled triangle
a1 = int (input("Enter side 1 "))
b1 = int (input("Enter side 2 "))
c1 = int (input("Enter side 3 "))
Num=[a1,b1,c1]
print(Num)
NumS=[]
NumS = sorted(Num)
h = NumS[2]
s1 = NumS[1]
s2 = NumS[0]
if ((h**2)==((s1**2)+(s2**2))) :
    print("Triangle forming sides ",h,s1,s2,"is a Right angled triangle")
else :
    print("Triangle forming sides ", h, s1, s2, "is NOT Right angled triangle")
print("**************************************************")
# Program to check whether year is leap year
y=int (input("enter year "))
if((y%100)==0 ) :
    if(y%400==0) :
        print("Leap Year")
    else :
        print("Not Leap Year")
else :
    if(y%4==0) :
        print("Leap Year")
    else :
        print("Not Leap Year")
#alternate method
if((y%4)==0 ) :
    if(y%100==0) :
        print("NOT Leap Year")
    else :
        print("Leap Year")
elif (y%400==0):
    print("Leap Year")
else :
    print("Not Leap Year")
print("**************************************************")
#tAKE 3 SIDES OF TRIANGLE AND check if equilateral , iscoscles or scalar
a1 = int (input("Enter side 1 "))
b1 = int (input("Enter side 2 "))
c1 = int (input("Enter side 3 "))
Num=[a1,b1,c1]
print(Num)
NumS=[]
NumS = sorted(Num)
h = NumS[2]
s1 = NumS[1]
s2 = NumS[0]
if(h==s1==s2) :
    print("Triangle forming sides ", h, s1, s2, "is Equilateral triangle")
elif(h!=s1!=s2) :
    print("Triangle forming sides ", h, s1, s2, "is Scalar triangle")
else :
    print("Triangle forming sides ", h, s1, s2, "is Isosceles triangle")
print("**************************************************")
#take year month , tell how many days in month
y = int(input("Enter year"))
m = int(input("Enter month no "))
ld=["X",31,28,31,30,31,30,31,31,30,31,30,31]

if((y%100)==0 ) :
    if(y%400==0) :
        print("Leap Year")
        ld[2]=29
        print("No of Days in month ",m," is ",ld[m])
    else :
        print("Not Leap Year")
        print("No of Days in month ",m," is ",ld[m])
else :
    if(y%4==0) :
        print("Leap Year")
        ld[2]=29
        print("No of Days in month ",m," is ",ld[m])
    else :
        print("Not Leap Year")
        print("No of Days in month ",m," is ",ld[m])
print("**************************************************")
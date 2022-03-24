#Function
#function to add 2 numbers
def addn(a,b) :
    "#add 2 numbers" #doc of function
    c=a+b
    print("sum of",a,"+",b,"=",c)
    return c

addn(1,2)
d=addn(12.5,2) # assign return c to d , withpout retuen you cant assign to d
print("d",d)

#write a program to add 3 numbers
e=int(input("enter num 1 " ))
f=int(input("enter num 2 " ))
g=int(input("enter num 3 " ))
h=e+f+g


#Nested
#using nestedfunctions
addn(addn(e,f),g) #2 prints will return ,nested ones and outer ones sum of
addn(e+f,g)
print(addn.__doc__) #prints documentation of function
print(len.__doc__) #prints documrntation of len function
#write a function with same  inputs , take input as a,b and return the maximum number
l,k,j =e,f,g
def greater(a,b) :
    "prints greater number "
    if (a>b) :
        c=a;
    else :
        c=b;
    print(c,"is greater among",a," & ",b)
    return(c)

greater(l,k)
greater(greater(l,k),j)

#to find factors
#Function to find odd or even
def oddeven(a2) :
    if (a2%2==0):
        print(a2," is even ")
        return("even")
    else :
        print(a2, " is odd ")
        return ("odd")
oddeven(l)
#calling of function within definition of another function
#write a program to check if a list contains even number
b1=[1,3,5,7,8,9,12,]
b2=[1,11,17,19]
def eveninlist(a1) :
    for i in a1:
        if (oddeven(i)=="even") :
            print("list contains even num , first occuring even num is ",i)
            break
    else :
        print("list not contain any even num")
eveninlist(b1)
eveninlist(b2)

"for i in a1:oddeven(i)"

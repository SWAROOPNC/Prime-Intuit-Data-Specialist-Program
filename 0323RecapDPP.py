#1 alpha input , check vowel of consonant
char = input("Enter character to check vowel or not ")
Vl =['a','e','i','o','u','A','E','I','O','U']
for l in Vl :
    if(char == l) :
        print(char ," is vowel ")
        break
else :
    print(char, " is consonant ")

#2 take angles of triangle as input , check if valid triangle or not
a1 = float(input("Enter first angle "))
a2 = float(input("Enter second angle "))
a3 = float(input("Enter third angle "))
if(a1+a2+a3==180) :
    print("Triangle comprising of angle ",a1,a2,a3," is a Valid Triangle")
else :
    print("Triangle comprising of angle ", a1, a2, a3, " is NOT Valid Triangle")

#2 take sides of triangle as input , check if valid triangle or not
a1 = float(input("Enter first side "))
a2 = float(input("Enter second side "))
a3 = float(input("Enter third side "))
#Sum of all any 2 sides , should be greater than other
if(a1<(a2+a3)) :
    if(a2<(a1+a3)):
        if(a3<(a1+a2)) :
            print("Triangle comprising of sides ", a1, a2, a3, " is Valid Triangle")
        else :
            print("Triangle comprising of sides ", a1, a2, a3, " is NOT Valid Triangle")
    else:
        print("Triangle comprising of sides ", a1, a2, a3, " is NOT Valid Triangle")
else :
    print("Triangle comprising of sides ", a1, a2, a3, " is NOT Valid Triangle")

# Take both low and high BP value and categorise as Hyper tension or Low BP
#ideal blood pressure is considered to be between 90/60mmHg and 120/80mmHg.
# high blood pressure is considered to be 140/90mmHg or higher.
# low blood pressure is considered to be 90/60mmHg or lower.
sys = int(input("Enter systolic or higher BP reading mmhg "))
dia = int(input("Enter systolic or higher BP reading mmhg "))

if(sys>120 or dia>90 ) :
    print("Patient have HyperTension")
elif(sys<90 and dia<60) :
    print("Patient have Low BP ")
else :
    print("Patient have normal BP")

#Take floor l*b,   tile size  , , calculate how many  tiles , required ,  if break consider take as 1 tile
print("enter floor details")
fl = float(input("Enter Length of floor "))
fb = float(input("Enter breadth of floor "))
print("enter tile details")
tl = float(input("Enter Length of tile "))
tb = float(input("Enter breadth of tile "))
AreaF = fl * fb
AreaT = tl * tb
print("Area of Floor ",AreaF)
print("Area of Tiles ",AreaT)
TI = AreaF/AreaT
print("Ideally Number of Tiles required is ",TI)
if((AreaF%AreaT)!=0 ) :
    print("No of Tiles Required is ",(AreaF//AreaT)+1)
else :
    print("No of Tiles Required is ", TI)

#5 calculate billing
#if <100 , free , next 100 u , 5 rs pu , after 200 , 10pu
u = float(input("Enter # of units consumed "))
if(u<100) :
    print("You need to pay nothing")
elif(u>200) :
    print("You have to pay Rs ",(100*5)+((200-u)*10))
else :
    print("You have to pay Rs ",(100-u)*5)


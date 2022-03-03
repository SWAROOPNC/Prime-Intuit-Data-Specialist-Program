a = float(input("Enter sugar level "))
i = 140
# standard
if (a>i) :
    print("patient is diabetic",a)
else :
    print("patient is non diabetic",a)
#case2 post pardinal & fast

# The blood sugar level is the amount of sugar present in the blood.
# This blood test is performed at two stages as F(fasting), PP(Post Prandial)
# F<110 normal, < 125 pre diabetic, 125+ diabetic
# https://www.mayoclinic.org/diseases-conditions/prediabetes/diagnosis-treatment/drc-20355284
# PP<140 normal, 180 pr diabetic

# https://www.emedicinehealth.com/high_blood_sugar_hyperglycemia/article_em.html

fs = float(input("Enter fasting sugar levels fs : "))
pps = float(input("Enter Post Prandial sugar levels pps : "))
if ((fs > 125) or (pps > 180)):
    print("Patient is Diabetic ")
else:
    print("Patient is Non Diabetic ")

# can use 2 nested if
fs = float (input ("Enter fasting sugar levels fs : "))
pps = float (input ("Enter Post Prandial sugar levels pps : "))
if (fs>110) :
    print("Patient is Diabetic ")
else :
    if(pps>140) :
        print("Patient is  Diabetic ")
    else :
        print("Non diabetic")
#Write a program to check whether the last digit of a number( entered by user )
#is  divisible by 3 or not.
n = input ("Enter number n : ")
nlast = n[-1]
nlastint = int(nlast)
print(n)
if (nlastint%3==0) :
    print("last digit of n is divisible by 3 ")
else :
    print("last digit of n is not divisible by 3 ")

#alternate method using divide and % 10
n = input ("Enter number n : ")
ne=n%10
if (ne%3==0) :
    print("last digit of n is divisible by 3 ")
else :
    print("last digit of n is not divisible by 3 ")

#To check last 2 diits dividde by 3  % 100
n = input ("Enter number n : ")
ne=n%100
if (ne%3==0) :
    print("last 2 digit of n is divisible by 3 ")
else :
    print("last 2 digit of n is not divisible by 3 ")

#To check middle of 3 digit is divisible by 3
n = input ("Enter 3 digit number n : "))
ne=int(n[1])
if (ne%3==0) :
    print("middle of 3 digit of n is divisible by 3 ")
else :
    print("middle of 3 digit of n is not divisible by 3 ")
#explore for any number of digit
#explore for any number of digit middle number%3
num = input ("Enter any digit number n : ")
print(num)
digit = len(num)
print(digit)
if(digit%2==0) :
    print("cant find middle number divisibility as even no of digits there  ")
else :
    digitm= (digit/2)+0.5
    digitm=int(digitm-1)
    print("digitm",digitm)
    nm = num[digitm]
    print(nm)
    print("middle number is ",nm)
    nm=int(nm)
    if (nm%3==0) :
        print("middle digit of the num of n is divisible by 3 ")
    else :
        print("middle digit of num  is not divisible by 3 ")

"""Write a program to print the discount and net payable amount:
Your working in an it department of a mega store, 
the store wants to run a discount of 5%
if the billing amount is less then Rs 1000 and 
10% discount 
if the billing value is greater then Rs 1000, 
you can except the billing amount as an input to begin with."""
b = float (input ("Enter billing amount to calculate discount "))
if (b<1000) :
    print ("Discount is 5%")
    print ("Net Payable Amount is ",0.95*b)
else :
    print ("Discount is 10%")
    print ("Net Payable Amount is ",0.9*b)
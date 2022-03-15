print(lambda x,y : x+[x[-1]+x[-2]]) #takes 2 input and
import functools
from functools import reduce
lx=[1,2,3,4]
"""print(functools.reduce(lambda x,y: x+y, lx))
print(functools.reduce(lambda x,y: x+[x[-1]+x[-2]], lx,[0,1])) #0,1 for initial x[-1,-2 value"""
#continue of fibonanci series
n=int(input("enter number of terms for fibonaci series "))
print(functools.reduce(lambda x,y: x+[x[-1]+x[-2]], range(0,n-2),[0,1])) #0,1 for initial x[-1,-2 value , n-2 + 0,1 = 10 digits

import NK_Math
from NK_Math import sub
x= int(input("enter a "))
y= int(input("enter b "))
p= NK_Math.add(x,y)
print(p)
p= NK_Math.sub(x,y)
print(p)
p= NK_Math.mult(x,y)
print(p)
p= NK_Math.div(x,y)
print(p)
#like functions , define variablesa in NKmath module , can call function and variables also
print(NK_Math.Message)
#coffee shop ,
#welcome message : to our shop
#wat like to have : coffee or tea #refer menu
#https://www.zomato.com/bangalore/namma-filter-coffee-jayanagar-bangalore
#our menu has beverages like Coffe Tea Milk , Please enter
#if coffe selected , print following types of coffe filter, black,
#please enter your selection
#ask for which milk , zerofat, toned, thick

#sugar , brown, jaggery,
#ask quantity
#store this module
#Main program call




# kind of coffe , size,small reg & large
#kind of roast , hot choclo , colt , capchino
#with milk or black
#sugar content
#order number random.ranint
#add price
#do in 2  files , modules contain value in , other front end execution
#
#
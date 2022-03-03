# what this program does
# what is the project name
# Date of creation
# Who created it

# change request number
# what is the chage
# who is doing this change
# date

"""This is not the right way to define multi line comments
Some people use triple quotes to define multi line comments"""

a = 1
print(id(a))

a = 10
b = 20
c = 30

print(a, b, c)

x, y, z = 10, 20, 30  # assign multiple  values in one line

print(x, y, z)

# Type casting the variables

a = 100
print(type(a))

b = str(100)
print(type(b))
print(b)

c = float (100)
print(c)
print(type(c))



# Operators

# + Addition
# - Subtraction
# * Multiplication
# / Division
# ** Exponent

a = 10
b = 20
# Addition
c = a+b
print(" a + b = ",c)

# Subtraction
c = b - a
print(" b - a = ",c)
# Multiplication
c = a * b
print(" a * b = ",c)

# Division
c = b / a
print(" b / a = ",c)

# Exponent
c = a **b
print(" a ** b = ", c)

"""SWAPPING PROGRAM """
a = float(input("Enter the 1st number "))
# any input is considered as string
b = float(input("Enter the 2nd number "))
print(a,b)
""" using temp variable """
temp=a
a=b
b=temp
print("after 1st swap using temp a,b ",a,b)
""" using multiple assignment variable """
a,b = b,a
print("after 2nd swap using mult assign a,b  ",a,b)
"""using addition menthod """
a=a+b
b=a-b
a=a-b
print("after 3rd swap using a+b meth a,b  ",a,b)
"""using sub a-b menthod """
a=a-b
b=a+b
a=-a+b
print("after 4th swap using a-b meth a,b  ",a,b)

"""using mult a*b menthod """
a=a*b
b=a/b
a=a/b
print("after 5th swap using a*b meth a,b  ",a,b)
"""using div a/b menthod """
a=a/b
b=a*b
a=b/a
print("after 6th swap using a/b meth a,b  ",a,b)
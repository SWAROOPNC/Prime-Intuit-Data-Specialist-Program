a=b=109
print(id(a))
print(id(b))
print(a is b)

c=110
d=110
print(id(c))
print(id(d))
print(c is d)
e=111
f=101
print(id(e))
print(id(f))
print(e is f)
e=f
print(id(e))
print(id(f))
print(e is f)
g=99.5
print(id(g))
h=99.57
print(id(h))
#variables in namespace
# numbers stored in same id
# 2 variables share same value mean same locztion
# is operator checks whether same memory location
#variables mapped to id
a ='swaroop is my name'
print('s' in a)

print('my ' in a)

print('zx' in a)

a=[1,2,3,4,5]
print(3 in a)
b=(2,4,6,8)
n=int(input("Enter single digit number "))
print(n in b)

t1=("abc",1,2,3,'red','soft',783.23)
print(t1)
print(type(t1))
l1= ['green','yellow','white',23,67]
print(l1)
print(type(l1))
t2 = tuple(l1) # typecasting list to tuprl
print(t2)
print(type(t2))
t3=()
print(t3)
#t3.append(3) will not work as immutable
#concatenation is allowed
t3=t1+t2
print(t3)
#accesing an element in tuple
print("t3[4]",t3[4])
#accesing elements with slicing
print("t3[2:6]",t3[2:6])
#access from begining
print("t3[:5]",t3[:5])
#access from end
print("t3[5:]",t3[5:])
#changing values within a tuple
# t3[4] =8 , it wont work , as tuples are immutable
#using repeat function on tuple
print("t2*3",t2*3)
print("t3[:3]*3",t3[:3]*3) #repeat part multiple times

t4= (('one',2),('two',2),("three" , 3),[4,5,6])
print("t4",t4) #nested tuple
print("t4[1]",t4[1])
print("t4[1][1]",t4[1][1])


l2= [[[1, 2, 3], [4, 5, 6]],[7,8,9],["a","b","c"]]
print("l2[0]",l2[0]) #nested list also allowed
print("l2[0][1]",l2[0][1])
print("l2[0][1][2]",l2[0][1][2])

#deleting a tuple
print(t2)
del(t2)
#print('t2',t2)
#can also use min and max functions
#print('max(t23)',max(t2)) #strings there
#clear means elements delete , variable name , structure still there ,
# but in delete tuple including variable will delete elements , print wont work in delete

#Tuple functions
print("t3",t3)
print('len(t3)',len(t3))
print("Membership function 'red' in t3",'red' in t3)
#tuple can be used for iteration
for x in t3 : print(x) # can write in same line for if simple

# List comprehension
l1=[1,2,3,4,5]
l2=[x**2 for x in l1] #observe the syntax
print('l2',l2)
l3=[x**3 for x in l1] #observe the syntax
print('l3',l3)

#using list comprehension to create a subgroup
l4= [x>2 for x in l1]
print("l4",l4)
l5= [x for x in l1 if x>2] #if x>2 only print
print("l5",l5)

#while loop
x = 10
while(x>0) :
    print(x)
    x=x-1
#can use while printing even numbers in a range
while x in range(0,10) :
    if (x%2 == 0) :
        print(x)
    x=x+1
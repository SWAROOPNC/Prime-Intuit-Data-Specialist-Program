l1 = [11,22,33,44,55,66,77,88,99,110] #Create List
l2 = [] # we can fill values to this list latter
print(l1)
print(type(l1))
print(l2)
l2.append(l1[0])
print(l1)
print(l2)
print(l1[:5])
print(l1[5:])
print(l1[::-1])

range(0,50,2) #wrong to create arrays
l3 = list(range(0,50,2)) # create step size
print(l3)
i=1
print(l1[i]) # indexing through variable prints l1[1]
i=i+1 # to iterate within a list
print(l1[i])

print(len(l1))

#alternate ways of FOr loop
i=0
print("New for 1")
for i in range(len(l1)) :
    print(l1[i])
    i=i+1

print("New for 2") #wo using i+1
for i in range(len(l1)) :
    print(l1[i])

print("New for 3") # wo using i

for num in l1 :
    print(num)
print("New for 4")
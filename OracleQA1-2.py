#1
#CHECK IF STR IS palindrome
str = str(input("Enter the string to check Palindrome or not "))
RevStr = str[::-1]
print("Original String : ",str)
print("rEVERSED String : ",RevStr)
if(str == RevStr) :
    print(str," is a palindrome ")
else :
    print(str," is NOT palindrome ")

#2
# find Missing Number in Arithmetic progression
#take input as list
li = input("Enter the input AP seperated by space ")
print(li)
lis=li.split(" ")
print(lis)
lil = []
#convert List string to list of int
for s in lis :
    lil.append(int(s))
print(lil)
lil.append(0)
lil.append(0)
for i in range(0,len(lil)) :
    if(lil[i+2] - lil[i+1] == lil[i+1]-lil[i]) :
        pass
    else :
        skip = i+2
        d=(lil[i+1]-lil[i])
        NewE = lil[i+1]+d
        print(skip)
        lil.insert(skip,NewE)
        print("Missing number is ",NewE,"at index",skip)
        break
lil.remove(lil[-1])
lil.remove(lil[-1])
print("Updated AP",lil)
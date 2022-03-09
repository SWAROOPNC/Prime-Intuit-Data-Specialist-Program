#DPP for today: given list 1 = [1,2,3,4,5,6,7,8,9,10]
#create list 2 containing square numbers of list1 and list 3  containing cubes of list 1
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [0,0,0,0,0,0,0,0,0,0]
list3 = [0,0,0,0,0,0,0,0,0,0]
print(list1)
print(list2)
print(list3)

for i in range(0,len(list1)) :
    list2[i] = (list1[i])**2
    list3[i] = (list1[i])**3

print(list1)
print(list2)
print(list3)

#DPP for today: given list 1 = [1,2,3,4,5,6,7,8,9,10]
#create list 2 containing square numbers of list1 and list 3  containing cubes of list 1
#ALTERNATE WAYS
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
list3 = []
print("list1",)
print(list2)
print(list3)

for i in range(0,len(list1)) :
    a = (list1[i])**2
    list2.append(a)
    b = (list1[i])**3
    list3.append(b)

print(list1)
print(list2)
print(list3)
# Python program to display all the prime numbers within an interval
#

lower1 = int(input("Enter the lower range : "))
upper2 = int(input("Enter the upper range : "))

print("Prime numbers between", lower1, "and", upper2, "are:")

for num in range(lower1, upper2 + 1):
    #print("num",num)
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            #print("i",i)
            #print("num%i",num%i)
            if (num % i) == 0:
                break
        else: # this is else for for loop
            print("prime # is",num)
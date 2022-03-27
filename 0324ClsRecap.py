X = "Life has no remote. Get Up and Change it Yourself"
#for remote [12:18]
Y = "Life" in X
print(Y)
#from Get Up to end [20:]
#entire sentence + yourself 2 times ,
#full sentence
print(X.find("Your"))
print(X+(2*(" "+X[41:])))
print(X[:19]+"\n"+X[20:])
print(len(X))
print(X.center(80,"0"))
#"0" fill char must be string , so
#The fill character must be exactly one character long
print(X.count('e',0,30))
s1=X.find(".")
print(X[:s1])
print(X[s1:])

X=[1,2,3,4]
print(str(X)) #retuens same list in string format "[1,2,3,4]"
#print(" ".join(X)) , Works only if elemtents are string not integer , for X list
X=["S","W","AROOP"]
print("".join(X))
print(" ".join(X))

y="Now is right time"
z="    Now is     "
z2 = "----Now is Right----"
print(y.strip())
print(z.strip())
print(z2.strip("-"))
#removes only leading and trailing whitespaces / specified char

#take input ans print words which has even length
X = "Life has no remote. Get Up and Change it Yourself"
Y=X.split(" ")
print(Y)
for word in Y :
    word=word.removesuffix(".")
    if((len(word))%2==0) :
        print(word+" "+str(len(word)))

#take str input , remove all duplicates
str1=str(input("ENter string "))
str2=str1.split(" ")
print(str2)
str6=[]
#if set is used , it will not be in order
for words in str2 :
    if (words not in str6) :
        str6.append(words)
print(str6)
print(" ".join(str6))
#print(str6.join(" ")) this is wrong
from collections import Counter
countsrt=Counter(str2)
strfinal = countsrt.keys()
print(strfinal)
#can join this and same steps

x = ['apple', 'banana', 'cherry']
y = enumerate(x)
#print 0 apple , 1 banana , 3 cherry
#program to perform sum upto n digits
n2 = int(input("Enter Num "))
s2=0
q2=0
for q2 in range(1,n2+1):
    s2=s2+q2 #or y+=y
print("Sum of ",n2,"numbers is",s2)

print(list(y))
#output [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
l2=[2,4]
l2.insert(2,4)
#2 is index , 4 is value 
print(l2)
import random
l4=[1,2,3,4,5,6,7,8,9]
random.shuffle(l4)
print(l4)
print(random.uniform(2,10))
#generates random float
print(random.randint(2,10))
print(random.random())
print(random.randrange(2,10,3))
#Program print all prime numbers between a given range
# Python program to display all the prime numbers within an interval
#

lower1 = int(input("Enter the lower range : "))
upper1 = int(input("Enter the upper range : "))

print("Prime numbers between", lower1, "and", upper1, "are:")

for num in range(lower1, upper1 + 1):
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

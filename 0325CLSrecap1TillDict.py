d1 = {1:"one",2:"two",3:"three"}
d2={"ones" : 5, "twos" : 10 , "threes" : 15 }
print(d1)
print(d2)
d1[4]="four"
print(d1)
print(d2)
d3={"Measures" : ("length","width","height"),"Values": (10,20,10)}
print(d3)
d4=dict(zip(d3["Measures"],d3["Values"]))
print(d4)

print(d1.keys())
print(d1.values())

print(d1[2])
print(d1.get(2)) #same as above , this prefered , to avoid mixing of syntax
print(d1.__getitem__(2))

print(d1.items()) #all items

print(len(d1))

d1.update(d2)
# d1=d1+d2 ,concatenation
print(d1)
print(d2)
d1.update({7: "seven", 8: "eight"}) #must add {}
#78 also concatenates to d1 dict
print(d1)

print(d1.pop("ones")) #returns value at ones
print(d1) #ones pair deleted

print(d1.popitem())
#pop one item in last not random #LIFO last in first out
print(d1)
#print(max(d1),min(d1)) error as values are strings

del d1[2]
print(d1)
d5 = list(reversed(d1)) #return keys in reverse order
print(d5)

s1={"a","e","i","o","u"}
s2={"a","b","c","d","e","f"}

print(s1) #out put not in order
#print(s1[1]) this not works , as not indexable
#isdisjoint , check if seperate sets
print(s1.isdisjoint(s2))
s3=frozenset({1,2,3,4,4,2,1,5,6,7,8,5})
print(s3)
#frozenset({1, 2, 3, 4})
print(s1.symmetric_difference(s2)) #gives out other than intersection , only unique elements in s1,s2
s2.add("g")
print(s2)
#can add or remove
s2.remove("g")
print(s1)
print(s2)
#s1.remove("h") , error , if not present
s1.discard("h") #if present , remove , if not no error and ignores
print(s1.pop())

d1={1:"one",2:"two",3:"three"}
#swap keys and values
d2=dict(zip(d1.values(),d1.keys()))
print(d1)
print(d2)
#can be done using function and list comprehension

#2 remove all duplicates from given sentence

#3 find sum of all values in a dict
d2={1:2,2:4,3:6,4:8}
sum1 =sum(d2.values())
print(sum1)
#3
#find if 2 sets intersect or one is subset or disjoint
s1={1,2,3,4,5,6,7,8,9}
s2={4,5,6,7,8,9}
if(s1.issubset(s2)) :
    print("s1.issubset(s2)",s1.issubset(s2))
elif(s2.issubset(s1)) :
    print("s2.issubset(s1)",s2.issubset(s1))

if(s1.issuperset(s2)) :
    print("s1.issuperset(s2)",s1.issuperset(s2))
elif(s2.issuperset(s1)) :
    print("s2.issuperset(s1)",s2.issuperset(s1))

if(s1.isdisjoint(s2)) :
    print("s1.isdisjoint(s2)",s1.isdisjoint(s2))
else :
    print("s1 s2 are not disjoint")
    print("S1 intersection s2 is ",s1.intersection(s2))
#5 find difference between 2 lists
l1 =[1,2,3,4,5,6]
l2=[4,5,6,7,8,9]
l1_l2 = set(l1).difference(set(l2))
print(l1_l2)
l2_l1 = set(l2).difference(set(l1))
print(l2_l1)

from collections import Counter
l3 = [15, 18, 14,'C#',18,15,'C#','C++','C++','Python',15]
rep  = Counter(l3)
print(rep)
#__ explore more underscoere underscoere funcrtions
#use capital letter counter
print(l1.__add__([7,8,9]))
#learn more about these __ functions
#l1.__getitem__()
#l1.__getattribute__()
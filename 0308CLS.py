l5 = [1,3,5,7]
print(l5)
l5.append(9)
print(l5)

#append add one data elemts
#clear - remove all elements
l5.clear()
print(l5)
l6=[2,4,6,8,'g','j']
l7=l6.copy()
print(l7)

#updating a copied list
l7.append(11)
print("l7",l7)
print("l6",l6)
#diff bw copy and = assign (deep copy)
# copy changes not reflect , # = changes , child list change also reflect in parent list
l8=l6
print("l6",l6)
l8.append("p")
print("l8",l8)
print("l6",l6) #note l6 also changed when l8 changed

#count function counts num of times a data is  repeated
l8.append(2)
print("l8",l8)
print("l8.count(2)",l8.count(2))

#extend is used to add any iterables ( list tuple string ) to end of
l9 = ['and','or','but']
print("l9",l9)
l9.extend(l8)
print("l9.extend(l8)" , l9)

s= "bright and sunny day "
l9.extend(s) # individual letters get add
print("l9.extend(s)", l9)

t1=(1,3,5)
l9.extend(t1)
print("l9.extend(t1)",l9)

#index function returns index number of value specified
print("l9.index('y')",l9.index('y'))

#insert to add value to mid or particular index  while replace or assign just replace
#here all other values in list are retained
l10=[i**2 for i in range(0,6)]
print("l10=[i**2 for i in range(0,6)]",l10)
l10[1]='x'
print("l10[1]='x'",l10)
l10.insert(1,1)
print("l10.insert(1,1):",l10)
#remove removes given value fro list
l10.remove('x')
print("l10.remove('x')",l10)
#pop removes given value from list , and  pop returns value removed
# useful to cross check removed in cource list
print("l10.pop(2) : ",l10.pop(2))
print("l10 after pop",l10)
l10.insert(2,4)
print("l10.insert(2,4)",l10)
#reverse , the order of dtat element in list
l10.reverse()
print("l10.reverse()",l10)
#sort function sorts the data  in ascending order
l10.sort()
print("l10.sort() ",l10)
print("max(l10)",max(l10))
print("min(l10)",min(l10))
print("l10",l10)
l11=l10.copy()
print("l11",l11)
#print("cmp(l10,l11",cmp(l10,l11)) , unavailable in version 3

# remove duplicates from list
l12 = [1,1,2,2,3,3,'a','b','c']
s1=set(l12)
print("s1=set(l12)",s1)
#set to list
l13=list(s1)
print("l13=list(s1)",l13)


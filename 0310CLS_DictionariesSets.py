d1={}
print("d1",d1)
d1["one"] = 1  #add elements to dic key and value
print("d1",d1)
d1['two'] = 2
d1['three'] = 3
print("d1",d1)
#alternate creation of dict
d2={'red': "apple", 'yellow': "banana", 'Black': "Grape"}
print("d2",d2)
print("d2['Black']",d2['Black'])
print("d2['red']",d2['red'])
#adding new values to dict
d2['green'] = "kiwi"
d2['purple'] = "Dragon"
print("d2",d2)
#d2[1]   , wrong , indexing wont work here

print("d2.keys",d2.keys())
print("d2.values()",d2.values())

#remove individual key value pair
del d2["purple"]
print("d2",d2)
# keep d2variable dict but remove all the values inside
d2.clear()
print("d2",d2)
#delete entire dict and d2 variable
#del d2 #
#print("d2",d2) d2 not defined
#dictionaries values can be same , keys should be unique , value can be duplicates , Keys are liek tuple , immutab le
#kwy cant be list , bcz list can be changed
print("type(d1)",type(d1))
#nested dictionary and lists / tuples
ind = {"rahul": {1: 23, 2: 34, 3: 56, 4: 45},
        'shikar': {1: 34, 2: 45, 3: 2, 4: 78}}
print("ind",ind)
print("ind['rahul'][1],ind['shikar'][1]",ind['rahul'][1],ind['shikar'][1])

#list inside dictionary
series = {'odi 1':[23,45,44,98,23,12],'odi 2':[34,98,34,17,0,6,19]}
print("series",series)
print("series['odi 1'][1],series['odi 2'][1]",series['odi 1'][1],series['odi 2'][1])

#tuple as key and value
dict3 = {(1,2):("one","two"),(3,4):("three","four")}
print("dict3",dict3)
print("dict3[(1,2)][1]",dict3[(1,2)][1]

#dict functions
print(dict3.items())
print(dict3.pop((1,2)))
#no pop , only remove

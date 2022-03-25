l1=[1,2,3,4,5,6,7,8,9]
print("l1",l1)

print(l3)
l2 = (lambda x : x%2 == 0  , l1 )
print("l2 = (lambda x : x%2 == 0  , l1 )",l2)
l2 = filter(lambda x : x%2 == 0  , l1 )
print("l2 = filter(lambda x : x%2 == 0  , l1 ) )",l2)
l2 = list(filter(lambda x : x%2 == 0  , l1 ))
print("l2 = list(filter(lambda x : x%2 == 0  , l1 )) )",l2)
"""l2 = tuple(filter(lambda x : x%2 == 0  , l1 ))
print("tuple(filter(lambda x : x%2 == 0  , l1 )",l2)""" #works for list , tuple and set too
#map vs filter vs reduce
l2 = list(map(lambda x : x**2 , l1 ))
print(l2)
l2 = list(filter(lambda x : x%3 == 0 , l1 ))
print(l2)
import functools
l3 = functools.reduce(lambda x,y : x+y , l1)

l3=map(lambda x:pow(x,3),l1)
print("l3=map(lambda x:pow(x,3),l1)",l3)
l3=list(map(lambda x:pow(x,3),l1))
print("l3=list(map(lambda x:pow(x,3),l1))",l3)
#map is more powerful compared to list compreension , map for any user defined function , LC create new list by passing iterale and expression
#map can be any complicated question
# in LC you wont call any function , u only specify the range
#LC most for creation list
#LC to be savewd and print , map reduxce can be print , LC returns only list ,
"""count =2
print(count)
#count = +1
count += 1 # auto increment
print(count)"""
from functools import reduce
sum = reduce(lambda x,y : x+y,l1)
print("sum = reduce(lambda x,y : x+y,l1)",sum)

#alternate way
"""
import functools 
sum = functools.reduce(lambda x,y : x+y,l1)
print("sum = reduce(lambda x,y : x+y,l1)",sum)
"""
from functools import reduce
"""fib = lambda n : reduce(lambda x : x+x[-1]+x[-2]),range(n-2)),[0,1]
print(fib(4))""" #not works
fib = lambda n: reduce(lambda x, y : x+[x[-1]+x[-2]],range(n-2), [0, 1])
print(fib(5))

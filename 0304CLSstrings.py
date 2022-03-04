"""Total 10 python units

Strings

Math functions
Lists
fibbonaci series
factorial
Tuple
list slicinf indexing

For while loops later
Break continue

Dictionary functions

Time stamps
Reading input output file creating new function
S3
start
HTML INSTEAD OF EXCEL
EXCEL LATER
Python no character data type
"""
name='Prime Intuit'
Phrase = "Prime Intuit is one of best finishing school"
multi_line = """ There was one boy named raju"""

print(name[0]) #single index
print(name[0:5]) # slicing
print(name[6:12]) #slicing from middle of text
print(name[:5]) # slicing from begin to certain length
print(name[5:]) #slicing from middle to end

#Reverse string
print(name[-1:5:-1]) # slicing in reverse order
print(name[9:5:-1]) #slicing witout using negative index
print(name[::-1]) #reversing entire string

#length function
print(len(name))
x=len(name)
print(x)

#concatenation
a="hello"
b="Prime Intuit"
c="Finishing School"
print(a+b+c)
print(a+b+" ! "+c)
d=a+b+" ! "+c
print(d)
print(3*a) # repeat 3 times
print((a+" ")*3) # repeat 3 times with space
print(((a+" ")*3) +b+" ! "+c)
print(((a+" ")*3) +b+" ! "+c+r"b/3"*3) #raw string
print(((a+" ")*3) +b[:6]+"!"+c) #CONCATENATION & slicing
#BUILT IN FUNCTION
#capitalize
x="there was a boy named raju"
print(x.capitalize()) # capitalise first letter
print(x.upper()) # capitalise full string
y=x.upper()
print(y)
print(y.lower()) # lower whole string
print(y.islower()) # check if y is lower
print(y.lower().capitalize()) # Use multiple functions lower + capitalise

#centr
print(b.center(80," ")) #80 page width , " " fill other sides
print(3000*"a") # use this get repetion operator
print(b.center(100,"+")) #80 page width , "+" fill other sides
print(d)
print(d.find("!")) #finds position
print(d.count("i")) # counts repetion
print(d.count("hello"))
print(d.count(" ",0,20)) #begin and end index to search

multi_line = """ There was one boy named raju"""
print(multi_line.find("raju"))#find index of raju
print(multi_line[25:29].capitalize())#index
print(multi_line.find("Raju"))#find index of space
print(multi_line.index("raju"))#find index of space
a="raju "
b="good boy"
print(a.join(b))#join same as concatenation but for list , tuple , not for string , so #not work
c=["raju"]
d=["   red   ","   blue is ","black     "]
print( " ".join(d))
e=" ".join(d)
print(e)
l2=e.strip( )
print(l2)
"""The strip() method returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed)."""
e= "      hello    swr    "
l3=e.strip()
print(e)
print(l3)
#is
#is
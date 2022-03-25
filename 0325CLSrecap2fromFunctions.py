#functions
#if indent needed colon must be there , ex def , if else
#object ca ne variable , function
#in function you can return object
#when there is repeted activity , again again , functions and to use somewhere else in other program or project
#one small repetitive act , for while
#function avoids rewriting in main code , can edit in module or def of func
def dupwords(str) :
    from collections import Counter
    l1=str.split(" ")
    fq = Counter(l1)
    print(fq)
    return(" ".join(fq))
#" "joins just joins keys

c = dupwords("Hai Swaroop Hai Again Gm Swaroop")
print(c)
#recursion where call of function can be called in return also
# where it has to come out is specified , if x=1 can be specified in def coed
# used in factorial , fibonanci series
"""def fact(a) :
    if(a>1) :
        return(a*fact(a-1))
print(fact(5))"""
#return vs yield  , return once returns , yield multiple values return
def DoubleGen(l1g) :
    for j in l1g :
        z=2*j
        yield z
l2g=[2,3,4]
cg=DoubleGen(l2g)
print("cg=DoubleGen(l2g) using yield : ",cg)
cg2=list(DoubleGen(l2g))
print("cg2=list(DoubleGen(l2g)) with yield : ",cg2)

import Transformation
print(Transformation.mtr2feet(1))
print(Transformation.kms2miles(1))
# we can define any data
print(Transformation.constant+100)
Transformation.constant = Transformation.constant +10
print(Transformation.constant)
#here value changed here only not in main Transformation
Transformation._constant = 100
print(Transformation._constant)
Transformation.__constant = 200
print((Transformation.__constant))
#__ idealy not allow change value , but it gives
from Transformation import __constant
print(__constant)
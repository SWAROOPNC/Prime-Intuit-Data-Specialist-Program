def Double(l1) :
    for i in l1 :
        i=2*i
        return i
l2=[2,3,4]
c=Double(l2)
print("c=Double(l2) using return",c)
#so just return first element in list
#Func GEn no syntacx difference , but return statement yield in gen , send i , back to loo[p , keep sending i back
#retuen VS yield , yield using gen
def DoubleGen(l1g) :
    for j in l1g :
        z=2*j
        yield z
l2g=[2,3,4]
cg=DoubleGen(l2g)
print("cg=DoubleGen(l2g) using yield : ",cg)
cg2=list(DoubleGen(l2g))
print("cg2=list(DoubleGen(l2g)) with yield : ",cg2)
#to work with any iterables lke list tuple , work with Range

n = int(input("Enter max range : " ))
def oddlist(n) :
    for k in range(0,n+1) :
        if(k%2 == 1) :
            yield k
print("list(oddlist(n)) ; ",list(oddlist(n)))

#write generation , list as input retuen cube of number , can do
# Take list l1 &l2 , third output product
l1=[1,2,3,4,5]
l2=[6,7,8,9,10,11,12,18]
def ProdList(l1,l2) :
    for i in range(0,min(len(l1),len(l2))) :
        a = (l1[i])*(l2[i])
        yield a

l3=list(ProdList(l1,l2))
print("l1",l1)
print("l2",l2)
print("l3",l3)

#Python File IO


#alternate way L: Not work
"""def ProdList2(l1i,l2i) :
    for i,j in l1i,l2i :
        k= i*j
        yield k
l3=list(ProdList2(l1,l2))
print(l1)
print(l2)
print(l3)"""
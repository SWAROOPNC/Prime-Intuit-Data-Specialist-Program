#print cumulative sum of a list
l5 = [10,20,30,40,50]
l5o=[]
x=0
for i in range(0,len(l5)) :
    l5o.append(l5[i]+x)
    x=l5o[i]
print(l5o)
print("***************************************")
#convert list of tuples into flat list
l6=[(1,2,3,),(3,4,5),(5,6,7)]
l7=[]
for ele in l6 :
    print(ele)
    for ele1 in ele :
        l7.append(ele1)
print(l7)
print("***************************************")
l1=[10,15,20,25,65,70,30]
l2=[0,1,2,0,1,2,0]
l2s=sorted(l2)
print(l1)
print(l2)
l3=zip(l2,l1)
l3s=sorted(l3)
print(l3s)
"""l3l=[]
for ele1 in l3s :
    for ele2 in ele1 :
        l3l.append(ele2)
print(l3l)
l3final = l3l[1::2]
print(l3final)"""
"""l3f = [x for _, for x in sorted(l3s)]"""
l3f = [y for x,y in l3s]
print(l3f)







print("***************************************")
#sort list of integers in descending order
l4=[-45,90,0,-30,10,15,20,25,65,70,30]
l4s=sorted(l4)
print(l4s)
l4r = l4s[::-1]
print(l4r)

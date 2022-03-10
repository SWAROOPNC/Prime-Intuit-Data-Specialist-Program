#sets=
s1={1,2,2,3,4,5,6}
print("input s1={1,2,2,3}")
print("result s1",s1)
s2={5,6,7,8,9}

print("s1.intersection(s2)",s1.intersection(s2))
s3=s1.union(s2)
print("s1.union(s2)",s1.union(s2))
print("s1.difference(s3)",s1.difference(s2))

print("s1.issubset(s3)",s1.issubset(s3))
print("s3.issuperset(s1)",s3.issuperset(s1))


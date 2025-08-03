a=(1,43,56,"imran",False,"mahmud",43)

num=a.count(43)
print(num)

i=a.index(56)
print(i)

repeat=a*2
print(repeat)

print(43 in repeat)
print(4 not in a)
print(len(repeat))

#slicing
slice=a[2:4]
print(slice)

#unpacking
x=[1,2,3]
a,b,c=x
print(a,b,c)
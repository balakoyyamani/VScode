#map(function, iterable)
a=[1,2,3,4,5]
b=[]
for i in a:
    b.append(i*i)
print(a)
print(b)
c=map(lambda x:x*x,a)
print(list(c))

names=["bala","siva","Irai"]
res=map(str.upper,names)
print(names)
print(list(res))
boo=map(lambda x:"Even" if x%2==0 else "Odd",a)
print(list(boo))

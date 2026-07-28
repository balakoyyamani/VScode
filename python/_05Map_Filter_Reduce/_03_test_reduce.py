from functools import reduce
n=[1,2,3,4,5]
res=reduce(lambda a,b:a+b,n)
print(res)
res1=reduce(lambda a,b:a if a>b else b,n)
print(res1)
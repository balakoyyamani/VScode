from functools import reduce
n=[1,2,3,4,5]
res=reduce(lambda a,b:a+b,
           filter(lambda x:x>10,
                  map(lambda i:i*i,n))
)
print(res)
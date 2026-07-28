import numpy as np
from numpy import random

a=np.array([1,2,3,4,5,6])
print("a =",a)
b=a.copy()
print("b =",b)
b[0]=100
print("a =",a)
print("b =",b)

print(a.shape)
new=a.reshape(2,3)
print(new)

n=random.randint(100,size=(3,5))
print(n)
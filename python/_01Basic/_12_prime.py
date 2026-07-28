n=int(input("Enter a number: "))
if n<2:
    print(n,"is not a prime number")  
    exit()  
flag=True
for i in range(2,n//2+1):
    if(n%i==0):
        flag=False
        break
if(flag):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
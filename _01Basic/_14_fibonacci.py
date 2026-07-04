n=int(input("Enter a number: "))
f=0
s=1
for i in range(1,n+1):
    print(f,end=" ")
    temp=f+s
    f=s
    s=temp
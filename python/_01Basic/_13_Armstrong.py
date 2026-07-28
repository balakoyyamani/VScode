n=int(input("Enter a Number: "))
temp=n
count=0;
while temp>0:
    count+=1
    temp//=10

sum=0
temp=n

while temp>0:
    digit=temp%10
    temp//=10
    sum+=digit**count

if sum==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")

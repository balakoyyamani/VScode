for i in range(5):
    print(i)

n=9394
print("Original number is:",n)
r=0
while n>0:
    r=(r*10)+(n%10)
    n//=10;

print("Reverse of the number is:",r)

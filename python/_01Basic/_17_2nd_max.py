n=[7,3,7,3,6,5,4,2,1]
def smax():
    m=n[0]
    sm=-2**31
    for i in range(len(n)):
        if(m<n[i]):
            sm=m
            m=n[i]
        elif(sm<n[i] and n[i]!=m):
            sm=n[i]
    return sm

print("Second Maximum:", smax())

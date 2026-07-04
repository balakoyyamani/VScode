n=[1,2,5,3,9,5,6,7,8]

def max_():
    m=n[0]
    for i in range(len(n)):
        if n[i]>m:
            m=n[i]
    return m

print("Maximum:", max_())
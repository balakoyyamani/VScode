a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

def add():
    return a+b
def sub():
    return a-b
def mul(c,d):
    return c*d
def div(c,d):
    return c/d

print("Addition:", add())
print("Subtraction:", sub())
print("Multiplication:", mul(5, 5))
print("Division:", div(5, 5))
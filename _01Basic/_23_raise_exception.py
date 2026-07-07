n=int(input("Enter the Age :"))

if n>=18:
    print("Eligible to Vote")
else:
    raise Exception("Not eligible to Vote")
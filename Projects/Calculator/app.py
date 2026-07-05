n1=int(input(": "))
result=0
while True:
    op=input("op:")
    n2=int(input(": "))
    match op:
        case "+":
            result=int(n1) + int(n2)
            print(result)
        case "-":
            result=int(n1) - int(n2)
            print(result)
        case "*":
            result=int(n1) * int(n2)
            print(result)
        case "/":
            result=int(n1) / int(n2)
            print(result)
        case "=":
            print(result)
        case "_":
            print("Enter the Valid operator")
            break

    n1=result

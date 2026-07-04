str=input("Enter a string: ")
match str:
    case "bala":
        print("Hello bala")
    case "hello":
        print("Hello world")
    case _:
        print("Hello everyone")
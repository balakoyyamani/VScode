class Animal:
    def __init__(self):
        print("This is an Animal class")
class Dog(Animal):
    def __init__(self):
        print("This is a Dog class")
        super().__init__()
class Cat(Animal):
    def __init__(self):
        print("This is a Cat class")
        Dog()
        super().__init__()

Cat()
Dog()
    
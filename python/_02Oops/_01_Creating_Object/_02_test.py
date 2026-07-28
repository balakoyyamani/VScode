class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)


s1=Student("balak",21)
s1.display()
s2=Student("Siva",21)
s2.display()
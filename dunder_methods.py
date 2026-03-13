class Car:
    def __init__(self, brand):
        self.brand = brand

c = Car("Toyota")

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s = Student("Umer")
print(s)

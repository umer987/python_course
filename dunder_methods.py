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



class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

obj = MyList([1,2,3,4])

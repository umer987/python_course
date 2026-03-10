# class FactoryKHI:
#     a ="this is KHI FACTORY ATTR"
#     def fun(self):
#         print("this is KHI FACTORY DEF")

# class FactoryISB(FactoryKHI):
#     pass
# obj = FactoryISB()
# print(obj.a)
# obj.fun()


#contructor in oops
# class Animal:
#     def __init__(self, name):
#         self.name= name
#     def ph(self):
#         print(f"YOUR NAME IS {self.name}")

# class Human(Animal):
#     pass

# obj = Human("umer")
# obj.ph()


class Animal:
    def __init__(self, name):
        self.name= name
    def ph(self):
        print(f"YOUR NAME IS {self.name} {self.age} ")

class Human(Animal):
    def __init__(self, name ,age):
        super().__init__(name)
        self.age =age

# obj1 =Animal("umer")
# obj1.ph()

obj = Human("umer" ,31)
obj.ph()



#types of inheritance
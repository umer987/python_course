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


# class Animal:
#     def __init__(self, name):
#         self.name= name
#     def ph(self):
#         print(f"YOUR NAME IS {self.name} {self.age} ")

# class Human(Animal):
#     def __init__(self, name ,age):
#         super().__init__(name)
#         self.age =age

# # obj1 =Animal("umer")
# # obj1.ph()

# obj = Human("umer" ,31)
# obj.ph()



#types of inheritance multiple inheritance
# class Animal:
#     a = "loin"

# class Human:
#     b="umer"

# class Robots(Human, Animal):
#     c="cc1"

# obj = Robots()
# print(obj.a, obj.b , obj.c)


#types of inheritance multilevel inheritance
class KhiFactory:
    def __init__(self , material , zips):
        self.material = material
        self.zips = zips
    def print_material(self):
        print(f"KHI FACTORY {self.material} {self.zips}")

class LhrFactory(KhiFactory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color
    def print_material_2(self):
        print(f"LHR FACTORY {self.material} {self.zips} {self.color}")


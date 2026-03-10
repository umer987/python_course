class Animal:
    def sound(self):
        return "bark"

class Cat(Animal):
    def sound(self):
        return "meow"
    
class Dog(Animal):
    def sound(self):
        return "bark"

animals =[Dog(), Cat(),Animal()]

for i in animals:
    print(i.sound())
    

class FactoryKHI:
    a ="this is KHI FACTORY ATTR"
    def fun(self):
        print("this is KHI FACTORY DEF")

class FactoryISB(FactoryKHI):
    pass
obj = FactoryISB()
print(obj.a)
obj.fun()
ok
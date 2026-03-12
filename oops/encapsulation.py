#starting encapsulation _single underscor isnot work in python python not support protected acces modifier
class Factory:
    _a = "KARACHI"

    def show(self):
        print("hello umer shakir")

class Factory2(Factory):
    b = "ISLAMABAD"

    def show2(self):
        print(super()._a)


obj = Factory2()

obj.show2()
#starting encapsulation _single underscor isnot work in python python not support protected acces modifier
# class Factory:
#     _a = "KARACHI"

#     def show(self):
#         print("hello umer shakir")

# class Factory2(Factory):
#     b = "ISLAMABAD"

#     def show2(self):
#         print(super()._a)


# obj = Factory2()

# obj.show2()


#only privete access modifier works in python and which is __ double underscore
class Factory:
    __a = "KARACHI"

    def __show(self):
        print("hello umer shakir")

class Factory2(Factory):
    b = "ISLAMABAD"

    def show2(self):
        print(super().__a)


obj = Factory2()


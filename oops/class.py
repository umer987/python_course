# class Factory:
#     a =12

#     def hello(self):
#         print("SYED MUHAMMAD UMER HELLO")

#     print("HOW ARE YOU")



#talk about object objects is also blueprint of class means obj = factory() all powers of factory class become in obj
# obj = Factory()
# print(obj.a)
# obj.hello() 


#constructor in opps we cant make class with paramaters like functions but we can do it by constructors 
class Factory:
    def __init__(self,material, zips, pockets):
        self.material = material
    

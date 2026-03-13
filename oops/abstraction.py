from abc import ABC , abstractmethod

class abstract(ABC):
    @abstractmethod
    def parameter(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class square(abstract):
    def __init__(self, side):
        self.side=side


class circle(abstract):
    def __init__(self,radius):
        self.radius=radius  
   
    def parameter(self):
        print("ok")
    

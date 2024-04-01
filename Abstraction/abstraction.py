from abc import ABCMeta , abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self):
        self.height = 21
        self.breadth = 7
        
    def printarea(self):    
        self.Box = self.height * self.breadth
        print(self.Box)
    
r = Rectangle()
r.printarea()
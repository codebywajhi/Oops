from abc import ABC, abstractmethod

class BaseClass(ABC):
    @abstractmethod
    def do_something(self):
        pass
    
    @abstractmethod
    def do_nothing(Self):
        pass

class Circle(BaseClass):
    def __init__(self):
        
        self.name = 5
        self.arm = 12
        
    def do_something(self):
        addition = self.arm + self.name
        return addition
    
    def do_nothing(self):
        pass
    
class Rectangle(BaseClass):
    def __init__(self):
        self.name = 15
        self.arm = 21
        
    def do_something(self):
        pass    
        
    def do_nothing(self):
        addition = self.arm * self.name
        return addition
    
c = Circle()
print(c.do_something)
R = Rectangle()
print(R.do_nothing)

    
        
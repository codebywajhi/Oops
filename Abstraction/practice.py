from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def circular_area(self):
        pass

    @abstractmethod
    def rectangular_area(self):
        pass

    @abstractmethod
    def triangular_area(self):
        pass

class Circular(Shape):    
    def __init__(self):
        self.radius = 18
        
    def circular_area(self):
        return 3.14 * self.radius * self.radius

class Rectangular(Shape):    
    def __init__(self):
        self.height = 1.05
        self.width = 2.00
        
    def rectangular_area(self):
        return self.height * self.width

class Triangular(Shape):    
    def __init__(self):
        self.height = 0.2 
        self.width = 0.50
        
    def triangular_area(self):
        return 0.5 * self.height * self.width

c = Circular()
print("Area of Circular:", c.circular_area())

r = Rectangular()
print("Area of Rectangular:", r.rectangular_area())

t = Triangular()
print("Area of Triangular:", t.triangular_area())





# from abc import ABCMeta , abstractmethod

# # BADR ABSTRACTED class

# class shape(metaclass = ABCMeta):
#     @abstractmethod
#     def circular_area(self):
#         return 0
#     @abstractmethod
#     def rectangular_area(self):
#         return 0
#     @abstractmethod
#     def triangular_area(self):
#         return 0
    
# class circular(shape):    
#     def __init__(self):
#         self.height=  15
#         self.width =  20
#         self.radius = 18
        
#     def circular_area(self):
#         return self.height * self.width * self.radius
# class Ractangular(shape):    
#     def __init__(self):
#         self.height=  1.05
#         self.width =  2.00
#         self.radius = 1.8
        
#     def rectangular_area(self):
#         return self.height * self.width * self.radius
# class Triangular(shape):    
#     def __init__(self):
#         self.height=  0.2 
#         self.width =  0.50
#         self.radius = 0.2
        
#     def triangular_area(self):
#         return self.height * self.width * self.radius
    
# c = circular()
# print(c.circular_area())
# r = Ractangular()
# print(r.rectangular_area())
# t = Triangular()
# print(t.triangular_area())
        
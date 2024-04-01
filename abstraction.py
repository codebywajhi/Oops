from abc import ABC, abstractmethod

# Abstract class defining the interface for a Shape
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    # Abstract method to calculate area
    @abstractmethod
    def calculate_area(self):
        pass

    # Abstract method to draw the shape
    @abstractmethod
    def draw(self):
        pass

# Concrete class implementing the Shape interface for a Circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def draw(self):
        print(f"Drawing a {self.color} circle with radius {self.radius}")

# Create a Circle object
circle = Circle("red", 3)

# Call methods on the Circle object
print("Circle Area:", circle.calculate_area())  # Output: Circle Area: 28.26
circle.draw()  # Output: Drawing a red circle with radius 3

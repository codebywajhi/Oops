# class Boxes:
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size
#         self.area_value = self.size ** 2  # Using a different variable name to store the area

#     def area(self):
#         return self.area_value

#     def define(self):
#         print(f"Color is {self.color} size is {self.size} area is {self.area()}")  # Calling self.area() to get the area

# class Box(Boxes):
#     def __init__(self, color, size):
#         super().__init__(color, size)

#     def area(self):
#         return self.size ** 2  # Calculate area based on size

#     def define(self):
#         super().define()

# class minibox(Boxes):
#     def __init__(self, color, size, area):
#         super().__init__(color, size)
#         self.additional_area = area  # Using a different variable name to store the additional area

#     def addition(self):
#         return self.additional_area + 5  # Returning the additional area plus 5

#     def define(self):
#         super().define()

# box = Box("Green", 21)
# box.define()

# m = minibox("Blue", 10, 12)
# m.define()

# class animal():
#     def sound(self):
#         print("this is an animal")
# class wolf(animal):
#     def sound(self):
#         print("Woou")
        
# b = wolf()
# b.sound()

                                                        # Multiple inheritance
                                                        
# class school():
#     def __init__(self,classes,sec):
#         self.classes = classes
#         self.section_name = sec

#     def section(self,quantity,grades):
#         self.quantities = quantity
#         self.grades = grades
        
#     def define(self):
#         print(f"so the classes are {self.classes} and section {self.section_name} quantities and grades are {self.grades} {self.quantities}")     

# class college():
#     def __init__(self,classes,sec):
#         self.classes = classes
#         self.section_name = sec

#     def section(self,quantity,grades):
#         self.quantities = quantity
#         self.grades = grades
        
#     def define(self):
#         print(f"so the classes are {self.classes} and section {self.section_name} quantities and grades are {self.grades} {self.quantities}")     
        
# class student_data(school , college):
#     def __init__(self):
#         super().__init__("AI third sem" , "A")
#     def section(self, quantity,grades):
#         super().section(quantity,grades)
#     def define(self):
#         super().define()  
#         print("Now Studing in a university with great attitude of learning with interest in book reading")
        
# s = student_data()
# s.section("5","A")
# s.define()


                                                            # Hybrid inheritance
                                                            

class A:
    def __init__(self,rooms,color):
        self.rooms = rooms
        self.color = color
    def kitchen(self,appliances):
        self.appliances = appliances
    def define(self):    
        print(f'This home has these rooms {self.rooms} with color {self.color}')
class B(A):
    def  __init__(self,rooms,color):
        super().__init__(rooms,color)
    def  bathroom(self,sanitary):
        self.sanitary = sanitary
        print(f"This home has sanitary {self.sanitary} with rooms  {self.rooms} with color {self.color}")

class C(A):
    def  __init__(self,rooms,color):
        super().__init__(rooms,color)
    def store(self,clothes):
        self.clothes = clothes
        print(f"There are {self.clothes} in the store with rooms  {self.rooms} with color {self.color}")
            
class D(B , C):
   def __init__(Self , rooms , color ):
        super().__init__(rooms,color)
   def bathroom(self,sanitary):
        super().bathroom(sanitary)
   def define(self):
        super().define()
        print(f"And this is my full home cuustody with room {self.rooms} color {self.color} sanitary {self.sanitary}")
        
b = B("2" , "red")
b.bathroom("brush")
c = C("5","blue , green")
c.store("pant")
d=D("6" , "yelowish")
d.bathroom("brush")
d.define()



# >.>>>  Polymorphism


class animal():
    def animals(Self):
        print("Hello Animals")
class cat(animal):
    def make_voice(self):
        print("meow")
class dog(animal):
    def make_voice(self):
        print("Bhow")
    
animals = [cat() , dog()]
for animal in animals:
    animal.make_voice()


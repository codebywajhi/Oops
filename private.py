class Car:
    def __init__(self, model):
        self.__model = model  # Private attribute

my_car = Car("Camry")
# This will raise an AttributeError: 'Car' object has no attribute '__model'
# print(my_car.__model)
# However, you can still access it using name mangling:
print(my_car._Car__model) 
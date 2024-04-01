class Car:
    def __init__(self, brand, model, year):
        self.brand = brand          # Public attribute
        self._model = model         # Protected attribute (convention)
        self.__year = year          # Private attribute

    # Getter methods
    def get_model(self):
        return self._model

    def get_year(self):
        return self.__year

    # Setter methods
    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        self.__year = year

# Create a Car object
my_car = Car("Toyota", "Camry", 2022)

# Accessing attributes directly
print("Brand:", my_car.brand)   # Output: Brand: Toyota
print("Model:", my_car._model)  # Output: Model: Camry
# Accessing private attribute directly will raise an AttributeError
# print("Year:", my_car.__year) # This line will raise an AttributeError

# Accessing attributes using getter methods
print("Model:", my_car.get_model())  # Output: Model: Camry
print("Year:", my_car.get_year())    # Output: Year: 2022

# Modifying attributes using setter methods
my_car.set_model("Honda")
my_car.set_year(2023)

# Accessing attributes after modification
print("Model:", my_car.get_model())  # Output: Model: Honda
print("Year:", my_car.get_year()) 
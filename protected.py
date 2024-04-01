class Car:
    def __init__(self, year):
        self._year = year  # Protected attribute (convention)

my_car = Car(2022)
print(my_car._year)  # Output: 2022

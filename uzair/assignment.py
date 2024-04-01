class Bill:
    def _init_(self, Username, HouseNo, oneunit=10 ):
        self.Username = Username
        self.HouseNo = HouseNo
        self.oneunit = oneunit
        self.energyconsumed = 0  # New data member to store energy consumed
        self.bill = 0  # New data member to store bill amount
        self.bill2 = 0  # New data member to store bill amount after due date
        print(f"Username: {Username}\nHouseNo: {HouseNo}\n")
        self.energyconsume()

    def energyconsume(self):
        category = input("Enter the category (A-D): ")
        if category in ["A", "B", "C", "D"]:
            if category == "A":
                self.energyconsumed = 1000
            elif category == "B":
                self.energyconsumed = 1200
            elif category == "C":
                self.energyconsumed = 1400
            elif category == "D":
                self.energyconsumed = 2000
            self.calculate_bill()
            print(f"Energy Consumed by {self.Username} is {self.energyconsumed}")
        else:
            print("INVALID CATEGORY, ONLY CHOOSE A-D")

    def calculate_bill(self):
        self.bill = self.energyconsumed * self.oneunit
        print(f"The bill generated to {self.Username} is: {self.bill}")
        print("After the due date, 10% tax will be added to your current bill")
        self.bill2 = self.bill + (self.bill * 0.1)
        print(f"The bill generated after the due date to {self.Username} will be: {self.bill2}")

    def record(self):
        with open("Bill.txt", "a") as f:
            f.write(
                f"The bill generated to User: {self.Username}, House No: {self.HouseNo}, is {self.bill}\n")

    def get_bill_amount(self):
        return self.bill

    def get_bill_amount_after_due(self):
        return self.bill2

    def get_energy_consumed(self):
        return self.energyconsumed


# Example usage
obj = Bill("Uzair", "Gulistan-e-Johar, Block 14, A-10")
obj.record()

# Accessing newly added methods
print("Bill Amount:", obj.get_bill_amount())
print("Bill Amount After Due Date:", obj.get_bill_amount_after_due())
print("Energy Consumed:", obj.get_energy_consumed())
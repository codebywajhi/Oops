class Bank:
    def __init__(self):
        self.Name = "wajhi"
        self.Address = "22f-10/b, Dhaka."
        self.Contact_information = "0317-1215017"
        self.Identification = "00-01"
        self.Date_of_Birth = "04-01-2004"
        self.Occupation = "Software Engineer"
        self.Account_Information = "Saving_Acount"
        self.Account_Number = "000123456"
        
        # Additional attributes
        self.Type_of_Account = "Savings"
        self.Account_Balance = 1000.00  # Example balance
        self.Interest_Rate = 0.02  # Example interest rate
        self.Account_Status = "Active"
        self.Account_Open_Date = "2023-01-01"  # Example open date
        self.Transaction_History = ["4500 ", "Withdrawal", "09-08-2023"]
        
        # Security attributes
        self.User_Authentication_Data = {
            "username": "wajhi123",
            "password": "********",
            "PIN": "1234"
        }
        self.Encryption_Keys = ["key1", "key2", "key3"]
        self.Security_Questions_Answers = {
            "What is your pet's name?": "Tommy",
            "What City were you born in?": "Dhaka",
            "What is your mother's maiden name?": "Khan"
        }
        
        self.Biometric_Data = {
            "Fingerprint": "xyz123",
            "Iris_Scan": "abc456"
        }
        
    def deposit(self, pin, deposit_amount):
        
        if pin != self.User_Authentication_Data["PIN"]:
            print("Invalid PIN")
            return
        if deposit_amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.Account_Balance += deposit_amount
        print(f"Deposit of {deposit_amount} successful. Current balance: {self.Account_Balance}")
        return self.Account_Balance
        
    def withdraw(self, pin, withdrawal_amount):
        if pin != self.User_Authentication_Data["PIN"]:
            print("Invalid PIN")
            return
        if withdrawal_amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if withdrawal_amount > self.Account_Balance:
            print("Insufficient funds.")
            return
        self.Account_Balance -= withdrawal_amount
        print(f"Withdrawal of {withdrawal_amount} successful. Current balance: {self.Account_Balance}")
        return self.Account_Balance


b = Bank()

code = input("Please Enter 1 for deposit and 2 for Withdrawal.")

if code not in ['1', '2']:
    print("Please Enter 1 for deposit and 2 for Withdrawal.") 
elif code == '1':
    pin = input("Please enter your PIN: ")
    b.deposit(pin, 500)  # Pass the PIN as an argument and deposit amount as an integer
elif code == '2':    
    pin = input("Please enter your PIN: ")
    b.withdraw(pin, 50)  # Pass the PIN as an argument and withdrawal amount as an integer

            
class HBL():
    def Accounts_type(self):
        self.credit = "Card by using that you can get the loan on transaction "
        self.debit = "Card by using which you can pay the amount you have on your current account "
    def personal_Account(self , balance ):
        self.balance = balance
        self.account = "Current_account"
        self.created = "Dec 2010"
        self.validity = 2029
        self.deposite = 4500
        self.transaction = 500
        
        self.current = self.balance - self.withdraw
    def Card_details(self , unioun_pay , active):
        self.card = unioun_pay
        self.active = active 
        
Bank = HBL()
Bank.Accounts_type(4000)
Bank.Card_details("Card type is Unioun Pay" , ' Active Account ')

want = input("Do you want balance type 1 : , For withdraw type 2 : ")

if want == "1" :
    print("your amount is this ")
    # print("f{self.balance}")
elif want ==  "2" :
    amount = input(" How much ? 1000 ? 2000 ? 3000 ?")
    if amount == balance :
        print(f"Your Amount is : {amount}")
    print("Your Balance is : {self.current}")     
else :
    print("Invalid Instruction")   
        
# class FAISAL():
#     def Accounts_type(self):
#         self.credit = "Card by using that you can get the loan on transaction "
#         self.debit = "Card by using which you can pay the amount you have on your current account "
#     def personal_Account(self ):
#         self.account = "Curent_account"
#         self.created = "Jan 2014"
#         self.balance = 4000
#         self.validity = 2029
#         self.deposite = 4500
#         self.transaction = 500
#     def Card_details(self , unioun_pay , active):
#         self.card = unioun_pay
#         self.active = active 
    
# class UBL():
#     def Accounts_type(self):
#         self.credit = "Card by using that you can get the loan on transaction "
#         self.debit = "Card by using which you can pay the amount you have on your current account "
#     def personal_Account(self ):
#         self.account = "current"
#         self.created = "dec 2010"
#         self.balance = 4000
#         self.validity = 2029
#         self.deposite = 4500
#         self.transaction = 500
#     def Card_details(self , unioun_pay , active):
#         self.card = unioun_pay
#         self.active = active 
    
# Bank = HBL()
# Bank.Accounts_type()
# Bank.Card_details("Card type is Unioun Pay" , ' Active Account ')

# ask = input("what is your Bank account name ?")
# want = input(" Do you want current cash , deposit or withdraw ? ")

# if want == balance :
#     print(self.balance)
# elif want == widthdraw :
#     amount = input(" How much ? 1000 ? 2000 ? 3000 ?")
#     print(f"Your amount is : {amount}")
#     print(" your Balance is : ")
    

# Bank1 = FAISAL()
# Bank1.Accounts_type()
# Bank1.Card_details("Card type is Visa Pay" , ' Active + Current Account')
# Bank2 = FAISAL()
# Bank2.Accounts_type()
# Bank2.Card_details("Its a Mater Card " , 'International Account Type')

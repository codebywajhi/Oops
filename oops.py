class duet():
    def __init__(self):
        self.n = "wajhi"
        self.s = "A_muqeem"
    def asking(self):
        self.name = input("Enter your Name")
        self.so = input("Your father Name")
    def providing(self):
        print(f"Name is {self.name} and Son Off {self.so}")
        
d1 = duet()
d1.asking()
d1.providing()                
        
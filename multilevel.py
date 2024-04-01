class wajhi:
    def __init__(self , name , passion ):
        self.name = name
        self.passion = passion
    def show(self):
        print(f"{self.name} {self.passion}")
class ali(wajhi):
    def __init__(self , name , passion ):
        wajhi.__init__(self , name , passion )
    def show(self):
        print(f"So here name is {self.name} and passion is {self.passion}")
class farhan(ali):
    def __init__(self , name , passion):
        ali.__init__(self , name , passion )
    def show(self):
        print(f"So here name is {self.name} and passion is {self.passion}")
class zohan(farhan):
    def __init__(self , name , passion ):
        farhan.__init__(self , name , passion)
    def show(self):
        print(f"So here name is {self.name} and passion is {self.passion}")
        
w = wajhi("wajhi" , " developer")
w.show()
a = ali("ali" ,"designer")
a.show()
f = farhan("farhan" , "sales man")
f.show()
z = zohan("zohan" , "students")
z.show()
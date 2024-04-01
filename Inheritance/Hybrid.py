class firstclass:
    def __init__(self):
        self.name = "Wajhi"
        
    def defyy(self):
        return(f"{self.name} is a good Boy!")
    
class Secondclass(firstclass):
    def __init__(self):
        firstclass.__init__(self)
        self.second_name = "Ali"
        
    def defyy(self):
        return(f" {self.name} and {self.second_name} is a good Boy!")
    
class Thirdclass(firstclass):
    def __init__(self):
        firstclass.__init__(self)
        self.two_name = "Wasay"
        
    def defyy(self):
        return(f" {self.name} and {self.two_name} is a good Boy!")
    
class Hybrid(Secondclass , Thirdclass):
    def __init__(self):
        Secondclass.__init__(self)
        Thirdclass.__init__(self)
        self.uni = "Dawood University"
        
    def explain(self):
        return(f" {self.name} , {self.two_name} and {self.second_name} are Best Friends they meet at {self.uni}")
    
f=firstclass()
f.defyy()    
s=Secondclass()
s.defyy()    
t=Thirdclass()
t.defyy()    
h=Hybrid()
print(h.explain())
    
class Mrone:
    def __init__(self , name , gender ):
        self.name = name
        self.gender = gender 
    def show(self):
        print(f"So name is {self.name} and gender is {self.gender}") 
class Mrtwo(Mrone):
    def __init__(self , name , gender ):
     Mrone.__init__(self ,name ,gender )
    def show(self):
        print(f"so name is {self.name} and gender is {self.gender}") 
class Mrthree(Mrone):
    def __init__(self , name , gender ):
     Mrone.__init__(self ,name ,gender )
    def show(self):
        print(f"so name is {self.name} and gender is {self.gender}") 
    
class twothree(Mrtwo , Mrthree):
    def __init__(self ,name1 , gender1 , name2 , gender2):
        Mrtwo.__init__(self, name1 , gender1)
        Mrthree.__init__(self, name2 , gender2)


O = Mrone("wajhi","male")
O.show()
M = Mrtwo("alian","male")
M.show()        
s = Mrthree("faryal","female")
s.show()        

t = twothree("Alian","Male","faryal","female")
print(f"{t.name}")
print(f"{t.gender}")
print(f"{t.name}")
print(f"{t.gender}")

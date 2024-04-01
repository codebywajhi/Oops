class myclass:
    def __init__(self):
        self.name = "Circle"
        self.cHeight = 8
        self.cwidth =  9
        self.clength = 10
    def priniting(self):
        self.Volume1 = self.cHeight * self.cwidth * self.clength
        return self.Volume1

class myclass2:
    def __init__(self):
        self.name = "Rectangle"
        self.rHeight = 9
        self.rwidth =  10
        self.rlength = 11
        
    def priniting2(self):
        self.Volume2 = self.rHeight * self.rwidth * self.rlength
        return self.Volume2        
    
class myclass3(myclass, myclass2):
    def __init__(self):
        myclass.__init__(self)
        myclass.priniting(self)
        myclass2.__init__(self)
        myclass2.priniting2(self)
        
    def inherited_prinitng(self):
        print(f"The Volume of a Circle is {self.Volume1} and volume of a Rectangle is {self.Volume2}")
    
m1 = myclass()
m1.priniting()
m2 = myclass2()
m2.priniting2()
m3 = myclass3()
m3.inherited_prinitng()        
        
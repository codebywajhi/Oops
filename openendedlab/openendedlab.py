class rectangular():
    def pressure(self ):
        self.height = 10
        self.width = 15
        self.radius = 20
        self.force = 12 
        Area = (3.142) * ( self.radius ** 2)
        self.Pressure = self.force / Area
        print(f"The pressure is {self.Pressure}  force per Area ")
    def volume(self ):
        self.height = 10
        self.breath = 12
        self.length = 5
        self.volume = self.length * self.breath * self.height 
        print(f"The volume of the container is {self.volume} cubic units")
class Circular():
    def pressure(self ):
        self.height = 10
        self.width = 12
        self.radius = 11
        self.force = 12 
        self.length = 15 
        Area = (3.142) * ( self.radius ** 2)
        self.Pressure =  ( self.force / Area ) + self.length
        print(f"The pressure is {self.Pressure}  force per Area ")
    def volume(self , ):
        self.height = 11
        self.breath = 21
        self.length = 13
        self.volume = self.length * self.breath * self.height 
        print(f"The volume of the container is {self.volume} cubic units")
        
r = rectangular()
r.pressure()
r.volume()
r = Circular()
r.pressure()
r.volume()
         
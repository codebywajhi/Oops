# Open Ended Lab
# >>
class rectangle():
    def volume(self , height , width , length):
        self.height = height 
        self.width = width 
        self.length = length 
        self.volume = self.height * self.width * self.length
        print(self.volume)
    def pressure(self , height , width , length , force ):
        self.height = height 
        self.width = width 
        self.length = length 
        self.force = force
        self.area = self.length * self.width 
        self.pressure = self.force / self.area
        print(self.pressure)

class Circular():
    def volume(self , pie , radius):
        self.pie = pie
        self.radius = radius
        self.volume = 2 * pie * self.radius
        print(self.volume)
    def pressure(self , height , width , length , force ):
        self.height = height 
        self.width = width 
        self.length = length 
        self.force = force
        self.area = self.length * self.width 
        self.pressure = self.force / self.area
        print(self.pressure)

r = rectangle()
r.volume(2,3,5)
r.pressure(3,5,5,12)
c = Circular()
c.volume(3.142,12)
c.pressure(5,10,5,15)
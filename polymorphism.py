# >.>>>  Polymorphism

# class animal():
#     def animals(Self):
#         print("Hello Animals")
# class cat(animal):
#     def make_voice(self):
#         print("meow")
# class dog(animal):
#     def make_voice(self):
#         print("Bhow")
    
# animals = [cat() , dog()]
# for animal in animals:
#     animal.make_voice()
    
# >>> second practice:

class solarsystem():
    def solar(self):
        print("There are many solae planets revolving around the sun ")
class sun(solarsystem):
    def size(self):
        print("Sun is the bigges plannet on earth")
class moon(solarsystem):
    def size(self):
        print("Moon give us the coolness on the soalr system and on the earth")
class mars(solarsystem):
    def size(self):
        print("Elon musk is searching live on mars")
class jupyter(solarsystem):
    def size(self):
        print("The raddish planet ever seen")
        
planets = [sun(),moon(),mars(),jupyter()]

for solarsystem in planets:
    solarsystem.size()
    

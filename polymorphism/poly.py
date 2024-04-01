class Papa:
    def __init__(self):
        self.Elderboy = "wajhi"
        self.Eldersister = "huma"
    def prinitng(self):
        print("both of them are brither sister")    
class Elderboy(Papa):
    def __init__(self):
        Papa.__init__(self)
    def prinitng(self):
        print(f"{self.Elderboy} is an Elder brother")    
class Eldersister(Papa):
    def __init__(self):
        Papa.__init__(self)
    def prinitng(self):
        print(f"{self.Eldersister} is Elder sister")
    
Papa = [Elderboy(),Eldersister()]

for i in Papa:
    i.prinitng()    
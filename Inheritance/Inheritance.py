class myone:
    def __init__(self):
        self.name = "wajhi"
        self.Class = "AI"
        self.agile = 12
        self.age2 = 4
    def print_number(self):
        Age =  self.agile * self.age2
        return Age

class mytwo(myone):
    def __init__(self):
        super().__init__()
    def printing_number(self):
        return  self.name + f" {self.Class} With Working as a Scientist and doing his game Inside! "

m = myone()
m.print_number()
M = mytwo()
print(M.printing_number())

        
class Elec:
    def __init__(self, Elec, ling):
        self.Elec = Elec
        self.ling = ling
        print(f"{Elec} and {ling}")

class AI:
    def __init__(self, ai, lang):
        self.ai = ai
        self.lang = lang 
        print(f"{ai} and {lang}")

class ElecAI(Elec, AI):
    def __init__(self, ai, lang, Elec, ling):
        Elec.__init__(self, Elec, ling)
        AI.__init__(self, ai, lang)

AB = ElecAI("Artificial intelligence", "python", "electronics", "multisim")
print(AB.ai)
print(AB.lang)


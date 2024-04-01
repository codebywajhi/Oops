class tune():
    def __init__(self):
        self._name = ""
    def getter(self):
        return  self._name
    def setter(self,value):
        self._name = value
        
t = tune()
t.getter()

t.setter("Wajhi ur Rehman")

print(t.getter())
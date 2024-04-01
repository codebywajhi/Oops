class my_class:
    def __init__(self , name , Mid):
        self._name = name
        self.__stage = Mid
    def getter_name(self):
        return self._name
    def getter_stage(self):
        return self.__stage
    def setter_name(self , name):
        self._name = name
    def setter_stage(self, stage):
        self.__stage = stage

m = my_class("wajhi","alice")

# Thats How We can Access the Private Attribute
print(m._my_class__stage)

print(f"name is : {m._name}")
m.getter_name()
m.getter_stage()

print("My Getter Name is :" +  m.getter_name())
print("My Getter Stage is :" + m.getter_stage())


m.setter_name("Aly")
m.setter_stage("DSP SINDH")


print("Setter Name is : " + m.getter_name())
print("Setter Stage is : " + m.getter_stage())



# Decorator : Decorator is a modifier of another function 

def intro(fx):
        print("Wajhi Here")
        fx()
def carear(fx):
        fx()
        print("He is an honest poerdon and always he tries to be in fit in his Friends")

@intro 
def greeting():
        print("He is an Honest Personality")
@carear
def name():
        print("WaJHI BABA")



# def greeting(fx):
#         print("Good Morning ")
#         fx()
# def thanks():
#         print("Nice to meet you Sir")
# def m_again(fx):
#         print("We Will Meet Again Sir here is My E-mail")
#         fx()
# def ouraddress(fx):
#         print("Our address is : ")
#         fx()

# @greeting
# def hello():
#         print("Hello Sir Wajhi")
# thanks()
# @m_again

# def ouremail():
#         print("mrwajhiqureshi@gmail.com")
# @ouraddress
# def address():
#         print("Area-P House no 410 Korangi no 2 1/2 Karachi Pakistan Asia")


# def greetings(name):
#         return "Hello " + name + " Good Morning"
# def inner(age):
#         return input("How are you Mr." + age)

# result = greetings("Wajhi")
# print(result)
# ask = inner("age of occupation ")
# print(ask)

# With Another Path 

# def Greeting(name):
#         def Hello():
#                 return " Hello " + name
#         return Hello
# result = Greeting(" Wajhi ")
# print(result)

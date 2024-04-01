c = int(input("Enter number to give you an attractive Deisgn!"))

a = 10
b = 11

try:
    
 if b != c:
    print ("Invalid Conditon")
 elif c >= a:
    print("Amazing")
 elif c <= a:
    print("-- Wow -- Everything is Set Here")
 elif c >= b:
    print("-- Glad! -- Everything is Set Here")
 elif c <= b:
    print("-- Walalh! -- Everything is Set Here")
    
except TypeError:
    print(TypeError("Invalid")) 
except SystemError:
    print(SystemError("Invalid")) 
except PendingDeprecationWarning:
    print(Warning("xxxxx")) 
else :
    print("Invalid Conditon")
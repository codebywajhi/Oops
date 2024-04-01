def pehlafunc(fx):
    num1 = 1 
    num2 = 2 
    sum = num1 + num2
    
    print(sum)
    fx()
def doosrafunc(fx):
    num1 = 1 
    num2 = 2 
    product = num1 * num2  
    
    print(product)
    fx()


@pehlafunc
def addition():
    print("So this is your master and you")
    
@doosrafunc
def prodition():
    print("So this is your master and you are mine ! ")
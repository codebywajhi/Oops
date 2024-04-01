def divide(x, y):
    try:
        result = x / y
        print("Division result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operand type(s) for division!")
    except Exception as e:
        print("An error occurred:", e)
        
divide(2,4
       )
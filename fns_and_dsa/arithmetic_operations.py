def perform_operation(num1,num2,operation):
    if operation=="add":
        return num1 + num2
    elif operation=="subtract":
        return num1 - num2
    elif operation=="multiply":
        return num1 * num2
    elif operation=="divide":
        if num2 > 0:
            return num1 / num2
        elif num2 == 0:
            return"Cannot divide by zero"
        elif num2 < 0:
            return"Choose a number greater than zero"
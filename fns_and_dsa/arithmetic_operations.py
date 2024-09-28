def perform_operation():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operation=input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation=="add":
        results=(num1 + num2)
        
    elif operation=="subtract":
        results=(num1 - num2)
        
    elif operation=="multiply":
        results=(num1 * num2)
        
    elif operation=="divide":
        if num2 > 0:
            results=(num1 / num2)
        elif num2 == 0:
            return"Cannot divide by zero"
        elif num2 < 0:
            return"Choose a number greater than zero"
            
            
    return results        
              
results=perform_operation()
print(results)
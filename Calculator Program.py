def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Math Error: Division by zero"

# Calculator function
def calculator():
    print("Edith's Calculator")
    
    # User input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    # Perform calculation based on user input
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        result = "Math Error: Invalid operator"
    
    # Display the result
    print("Result: ", result)

# Run the calculator
calculator()


import math

# Function to perform basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to perform scientific operations
def scientific_calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Exponentiation")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    elif choice in ['5', '6', '7', '8', '9']:
        num = float(input("Enter a number: "))
        if choice == '5':
            print("Result:", math.sqrt(num))
        elif choice == '6':
            exponent = float(input("Enter the exponent: "))
            print("Result:", math.pow(num, exponent))
        elif choice == '7':
            print("Result:", math.sin(math.radians(num)))
        elif choice == '8':
            print("Result:", math.cos(math.radians(num)))
        elif choice == '9':
            print("Result:", math.tan(math.radians(num)))
    else:
        print("Invalid input")

# Call the scientific calculator function
scientific_calculator()

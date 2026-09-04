import math
print("Welcome to the calculator!")
print("Available operations: +, -, *, /, sqrt, pow")
def calculator():
    while True:
        operation = input("Enter operation (or 'exit' to quit): ")
        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif operation in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        print("Error: Division by zero is not allowed.")
                        continue
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif operation == 'sqrt':
            try:
                num = float(input("Enter a number: "))
                if num >= 0:
                    result = math.sqrt(num)
                    print(f"Result: {result}")
                else:
                    print("Error: Cannot calculate square root of a negative number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif operation == 'pow':
            try:
                base = float(input("Enter the base number: "))
                exponent = float(input("Enter the exponent: "))
                result = math.pow(base, exponent)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid operation. Please try again.")
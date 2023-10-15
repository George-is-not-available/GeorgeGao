def add(a, b):
    result = a + b
    print("Addition result:", result)


def subtract(a, b):
    result = a - b
    print("Subtraction result:", result)


def multiply(a, b):
    result = a * b
    print("Multiplication result:", result)


def divide(a, b):
    if b != 0:
        result = a / b
        print("Division result:", result)
    else:
        print("Division by zero error.")


a = float(input("Enter a number......"))
b = float(input("Enter a number......"))
operation = input("Enter an operation (+, -, *, /)......")

if operation == "+":
    add(a, b)
elif operation == "-":
    subtract(a, b)
elif operation == "*":
    multiply(a, b)
elif operation == "/":
    divide(a, b)

'''
Progrma name: Calculator
Author: Imran Hunter
Description: This is a calculator that can also handle invaild inputs
'''

#Main function
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def floor_divide(a, b):
    return a // b

#Convert input to number
def convert_number(value):
    try:
        if '.' in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        return None

#Main program
print("Please enter an Expression (or type 'quit' to exit):")

while True:
    expr = input(":> ").strip()

    if expr.lower() in ["quit", "q"]:
        print("Calculator exited.")
        break

    parts = expr.split()

    if len(parts) != 3:
        print(f"Error: Invalid Expression - ({expr})")
        continue

    left, op, right = parts

    left = convert_number(left)
    right = convert_number(right)

    if left is None or right is None:
        print(f"Error: Invalid Expression - ({expr})")
        continue

    try:
        if op == "+":
            result = add(left, right)
        elif op == "-":
            result = subtract(left, right)
        elif op == "*":
            result = multiply(left, right)
        elif op == "/":
            result = divide(left, right)
        elif op == "%":
            result = modulus(left, right)
        elif op == "**":
            result = power(left, right)
        elif op == "//":
            result = floor_divide(left, right)
        else:
            print(f"Error: Invalid Operator - ({op})")
            continue

        print(f"Result: {left} {op} {right} = {result}")
    except ZeroDivisionError:
        print("Error: Invalid Expression - ({expr})")
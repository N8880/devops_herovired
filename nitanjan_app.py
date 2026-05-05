def greet(name):
    return f'Hello, {name}!'

print(greet('World')
# Feature 2: Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# Simple interactive menu
print("=== Calculator ===")
print(f"Add:      {add(10, 5)}")
print(f"Subtract: {subtract(10, 5)}")
print(f"Multiply: {multiply(10, 5)}")
print(f"Divide:   {divide(10, 5)}")

# Feature 3: Temperature converter
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("\n=== Temperature Converter ===")
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"98.6°F = {fahrenheit_to_celsius(98.6)}°C")

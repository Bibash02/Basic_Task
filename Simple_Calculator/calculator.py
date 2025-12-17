
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error!")
    else:
        return a / b

while True:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    print("Select operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print(f"Addition: {add(num1, num2)}")
    elif choice == '2':
        print(f"Subtraction: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Multiplication: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Division: {divide(num1, num2)}")
    else:
        print("Invalid choice!")

# Creating Function
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
        return "Error: Division by zero"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")



    if choice == "1":
        print(f"Result: {add(a, b)}")
    elif choice == "2":
        print(f"Result: {subtract(a, b)}")
    elif choice == "3":
        print(f"Result: {multiply(a, b)}")
    elif choice == "4":
        print(f"Result: {divide(a, b)}")
    else:
        print("Invalid choice!")

    if choice == "5":
        print("Exiting calculator. Goodbye!")
        break


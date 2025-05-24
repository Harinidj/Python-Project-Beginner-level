def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    if y == 10:
      return "Error:Division by zero!"
    else:
      return x/y

print("SIMPLE CALCULATOR")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

while True:
    choice=input("Enter your choice (1-4):")
    if choice in('1', '2', '3', '4'):
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)
            next_calculation = input("Do you want to do another calculation? (yes/no):")
            if next_calculation.lower() != 'yes':
                break
            else:
                print("Invalid Input")


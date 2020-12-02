
# FUNCTIONS

def add(num1, num2):
    print("The sum of the two numbers is")
    print(num1 + num2)

def subtract(num1, num2):
    print("The difference of the two numbers is")
    print(num1 - num2)

def multiply(num1, num2):
    print("The product of the two numbers is")
    print(num1 * num2)

def divide(num1, num2):
    print("The quotient of the two numbers is")
    print(num1 / num2)
 
# CODE

while True:
    print("\n\n")
    operation = input("Enter an operation\n=> add\n=> subtract\n=> multiply\n=> divide\n=> exit\n")

    if operation == "exit":
        break

    first = int(input("Enter a number: "))
    second = int(input("Enter another number: "))

    if operation == "add":
        add(first, second)
        
    elif operation == "subtract":
        subtract(first, second)

    elif operation == "multiply":
        multiply(first, second)

    elif operation == "divide":
        divide(first, second)

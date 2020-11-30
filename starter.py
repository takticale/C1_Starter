
# FUNCTIONS

def add(num1, num2):
  print(num1 + num2)
 
# CODE

operation = input("Enter an operation\n=> add\n=> subtract\n=> multiply\n=> divide\n")
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

if operation == "add":
  print("The sum of the two numbers is")
  add(first, second)

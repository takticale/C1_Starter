
# FUNCTIONS

def add(num1, num2):
  print(num1 + num2)
 
# CODE

operation = input("Enter an operation\n=> add\n=>subtract\n=>multiply\n=>divide\n")
first = input("Enter a number")
second = input("Enter another number")

if operation == "add":
  add(first, second)

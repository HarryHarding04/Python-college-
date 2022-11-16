def multiplication(a, b):
  total = (a * b)
  print(total)

def addnum(a, b):
  total = (a + b)
  print(total)

def subtract(a, b):
  total = (a - b)
  print(total)

def division(a, b):
  total = (a / b)
  print(total)

def modulo(a, b):
  total = (a % b)
  print(total)

function = input("what function would you like to perform? ")

if function == ("*"):
  num1 = int(input("what is your first number: "))
  num2 = int(input("what is your second number: "))
  multiplication(num1, num2)

if function == ("+"):
  num1 = int(input("what is your first number: "))
  num2 = int(input("what is your second number: "))
  addnum(num1, num2)

if function == ("-"):
  num1 = int(input("what is your first number: "))
  num2 = int(input("what is your second number: "))
  subtract(num1, num2)

if function == ("/"):
  num1 = int(input("what is your first number: "))
  num2 = int(input("what is your second number: "))
  division(num1, num2)

if function == ("%"):
  num1 = int(input("what is your first number: "))
  num2 = int(input("what is your second number: "))
  modulo(num1, num2)
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
num3 = int(input('Enter your third number: '))
total = (num1 + num2 + num3)
if num1 == num2 or num2 == num3 or num3 == num1:
    total = (0)
print('The total is', total)

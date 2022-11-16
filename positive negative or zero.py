running = True

while running == True:

    num = float(input('Enter a number: '))

    if num > 0:
        print('Your number is positive')
    if num == 0:
        print('Your number is zero')
    if num < 0:
        print('Your number is negative')

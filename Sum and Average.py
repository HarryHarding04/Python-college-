loop = int(input('How many numbers would you like to input?'))

output = 0

for i in range (0, loop):
    number = int(input('Input a number you would like to use'))
    output += number


average = output/loop

print('The sum is: ', output, 'The average is: ', average)

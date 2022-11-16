a = '1'
b = '2'
c = '3'
d = '4'
e = '5'
space = " "

def separate():
    print('')
    print('***************')
    print('')


separate()
print(a)
print(b*2)
print(c*3)
print(d*4)
print(e*5)

separate()

for i in range(1,6):
    for j in range(i):
        print(i, end=' ')
    print('')

separate()

row = 5

for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end='')
    print('')

separate()
    
lst = []

def numadd():
    running = True
    while running == True:
        try:
            num = int(input(''))
            lst.append(num)
        except ValueError:
            running == False
            print(sum(lst))
            break
numadd()

separate()

def increase():
    running = True
    while running == True:
        try:
            num = int(input(''))
            num += 1
            print(num)
        except ValueError:
            break
increase()

separate()

def triarea():
    running = True
    while running == True:
        try:
            base = int(input('Base: '))
            height = int(input('Height: '))
            print('Area:', base * height / 2)
        except ValueError:
            break
triarea()

separate()

def remainder():
    running = True
    while running == True:
        try:
            num1 = int(input('First number: '))
            num2 = int(input('Second number: '))
            print('remainder:', num1 % num2)
        except ValueError:
            break
        
remainder()


    



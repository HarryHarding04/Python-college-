
winter = ['December', 'January', 'February', 'March']
spring = ['April', 'June']
summer = ['July', 'August', 'September']

month = input('Input the month: ')
day = int(input('Input the day: '))

if month in winter:
    if month == ('December'):
        if day < 21:
            print('It is Fall')
        else:
            print('It is Winter')
    if month == ('March'):
        if day < 20:
            print('It is Winter')
        else:
            print('It is Spring')
if month in spring:
    if month == ('June'):
        if day < 20:
            print('It is Spring')
        else:
            print('It is Summer')
    else:
        print('It is Spring')
if month in summer:
    if month == ('September'):
        if day < 22:
            print('It is Summer')
        else:
            print('It is Fall')
    else:
        print('It is Summer')

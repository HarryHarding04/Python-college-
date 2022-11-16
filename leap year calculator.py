running = True

while running == True:

    year = int(input("Enter a year: "))

    if (year % 4 == 0) and (year % 400 != 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
    

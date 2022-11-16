import sys
import datetime
import calendar
from datetime import date

def task1():
    print("Twinkle, twinkle, little star,")
    print("	   How I wonder what you are!")
    print("                Up above the world so high,")
    print("                Like a diamond in the sky.")
    print("Twinkle, twinkle, little star,")
    print("        How i wonder what you are")

task1()

def task2():
    print(sys.version)

task2()

def task3():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    

task3()

def task4():
    r = 4.5
    pi = 3.14
    area = (r * pi)**2
    print(r)
    print(area)

task4()

def task5():
    fname = "Harry"
    lname = "Harding"
    fname, lname = lname, fname
    print(fname, lname)

task5()

def task6():
    nums = 1,2,3,4
    mylist = nums
    mytuple = nums
    print(mylist)
    print(mytuple)

task6()

def task7():
    filename = input("Input the Filename: ")
    f_extns = filename.split(".")
    print ("The extension of the file is : " + repr(f_extns[-1]))

def task8():
    color_list = ["Red","Green","White" ,"Black"]
    print( "%s %s"%(color_list[0],color_list[-1]))

def task9():
    exam_st_date = (11,12,2014)
    print( "The examination will start from : %i / %i / %i"%exam_st_date)

def task10():
    a = int(input("Input an integer : "))
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) )
    print (n1+n2+n3)

def task11():
    print(abs.__doc__)


def task12():
    y = int(input("Input the year : "))
    m = int(input("Input the month : "))
    print(calendar.month(y, m))

def task13():
    print("""
    a string that you "don't" have to escape
    This
    is a  ....... multi-line
    heredoc string --------> example
    """)

def task14():
    f_date = date(2014, 7, 2)
    l_date = date(2014, 7, 11)
    delta = l_date - f_date
    print(delta.days)

def task15():
    pi = 3.1415926535897931
    r= 6.0
    V= 4.0/3.0*pi* r**3
    print('The volume of the sphere is: ',V)


def task16(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

def task17(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

    

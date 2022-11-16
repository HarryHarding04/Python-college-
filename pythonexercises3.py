#Question 1
def cube():
    x = int(input("Input a number: "))
    z = x+1
    for i in range(1, z):
        print("Current Number is :", i, "and the cube is", i**3)

#Question 2
def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])
lst = []
lst.extend(mylist)
print(lst)

#Question 3
lsrt=[]
for x in range(2000, 3200):

    if (x%7==0) and (x%5==0):
        lsrt.append(str(x))
print('2000,',','.join(lsrt),',3200')





#Question 4
passwd = input('please enter password: ')     

def password_check(passwd):
    SpecialSym =['$', '@', '#', '%']
    val = True

    if len(passwd) < 6: 
        print('length should be at least 6')
        val = False

    if len(passwd) > 12: 
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols $@#%')
        val = False
    if val: 
        return val

password_check(passwd)

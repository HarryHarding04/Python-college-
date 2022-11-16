z = [3, 6, 8, 22, 34]
print(min(z))
print(max(z))

age = [12, 23, 30, 35, 42, 48]
print(age)
print(age[3])
age.append(33)
print(age)
age.remove(12)
print(age)
print(max(age))
age.insert(1, 12)
print(age)
age.insert(33, 99)
print(age)
print(age.count(42))
age.append(33)
print(age.count(33))
print(len(age))

door = ("closed")

while (len(age)) == 9:
    door = ("open")

if door == "open":
    print("do you wish to enter the door? ")

answer = input()

if answer == "yes":
    print("okay")


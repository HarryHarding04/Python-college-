age = int(input("Age of the dog: "))
print()
if age < 0:
    print("this cannot be true")
elif age == 0:
    print("this corresponds to 0 human years")
elif age == 1:
    print("Roughly 14 years")
elif age == 2:
    print("Approximately 22 years")
else:
    human = 22 + (age -2) * 5
    print("corresponds to " + str(human) + " human years")

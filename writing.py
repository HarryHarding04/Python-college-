f = open("yeah.txt", "w")
x = input()
f.write(x)
f.close

f = open("yeah.txt")
print(f.read())

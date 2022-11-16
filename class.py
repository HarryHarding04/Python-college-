class User:
  def __init__(self, fullname, birthday, snumber, phonenum, age, nationality, eyecolour, haircolour, height, birthplace):
    self.name = fullname
    self.birthday = birthday
    self.snumber = snumber
    self.phonenum = phonenum
    self.age = age
    self.nationality = nationality
    self.eyecolour = eyecolour
    self.haircolour = haircolour
    self.height = height
    self.birthplace = birthplace 

user1 = User("Harry Harding", "04122004", 20239242, "07570047284", 16, "English", "blue", "blonde", "6", "England")
user2 = User("Matt Greenwood", 14032004, 20236522, "07275679135", 16, "English", "brown", "brown", "5'11", "Farnborough")
user3 = User("Joe Sansbury", 11112004, 23458621, "07561289022", 16, "English", "blue", "brown", "5'10", "portsmouth")

print(user1.name)
print(user1.birthday)
print(user1.snumber)
print(user1.phonenum)
print(user1.age)
print(user1.nationality)
print(user1.eyecolour)
print(user1.haircolour)
print(user1.height)
print(user1.birthplace)
print(" ")
print(user2.name)
print(user2.birthday)
print(user2.snumber)
print(user2.phonenum)
print(user2.age)
print(user2.nationality)
print(user2.eyecolour)
print(user2.haircolour)
print(user2.height)
print(user2.birthplace)
print(" ")
print(user3.name)
print(user3.birthday)
print(user3.snumber)
print(user3.phonenum)
print(user3.age)
print(user3.nationality)
print(user3.eyecolour)
print(user3.haircolour)
print(user3.height)
print(user3.birthplace)
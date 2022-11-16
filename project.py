print('an integer can only be displayed as a full number.')
print('a float displays the full number and the decimal value.')
num = (1.2)
print(int(num))
print(float(num))

print('a string can display any amount of characters as long as they are not numbers.')
print('have to put quotation or speech marks around the letter or word you type.')
word = ("Hello")

print('numbers can have many data types such as:')
print("int")
print("float")

print('python has 6 different sequence types. they are:')
print('strings:')
print(str(word))
print('lists:')
print('there are different types of lists')
print('list of integers:')
my_list = [1, 2, 3]
print(my_list)
print('empty lists:')
print('empty_list = []')
print('lists with mixed data types')
mixed_list = [1, "Hello", 3.2]
print(mixed_list)
print('and nested lists:')
nested_list = ["mouse", [8, 4, 6], ['a']]
print(nested_list)
print('tuples:')
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))
print('byte sequence:')
string = ('a byte string is a sequence of bytes. it is not human readable')
print(string)
arr = bytes(string, 'ascii')
print(arr,'\n')
for byte in arr:
    print(byte, end=' ')
print("\n")
print('byte arrays:')
prime_numbers = [2, 3, 5, 7]
byte_array = bytearray(prime_numbers)
print(byte_array)
print('range():')
x = range(6)
for n in x:
    print(n)
print('dictionary:')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print('mutable and immutable objects:')
print("a mutable object can be changed after it is created, and an immutable object can't.")
print("immutable objects are built in types like int, float, bool, tuple, unicode")
print("mutable objects are built in types like list, set, dict")

a = [6]

b = [9]

def swap(a, b):
    temp = b
    b = a
    a = temp
    return(a, b)

print('a =', a)
print('b =', b)
[a, b] = swap(a, b)
print('a =', a)
print('b =', b)



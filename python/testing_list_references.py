a = 3
b = a
print(id(a) == id(b))
a = 4
print(a, b, (id(a) == id(b)))
b = 4
print(id(a) == id(b))


a = [12]
b = [12]
print(id(a) == id(b))
a.append(3)
print(a)
print(b)
print(id(a) == id(b))
b = a
b.append(4)
print(a, b, sep=" | ")
print(id(a) == id(b))

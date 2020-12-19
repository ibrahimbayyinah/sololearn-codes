# below is how you'd do it with list comprehension:
a = ["value{x}".format(x=i) for i in range(1, 101)]
print(a)

print('\n ----------------------------------- \n') # just printing a seperation between the 2 methods

# and here is how to do it using a dictionary:
b = {}
j = 1
while j <= 100:
    key = j
    value = "value{}".format(j)
    b[key] = value
    j += 1
print(b)

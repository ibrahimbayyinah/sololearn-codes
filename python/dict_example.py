pairs = {1: "apple",
    "orange": [2, 3, 4], 
    True: False, 
    None: "True",
    "orange": [2, 2, 2]
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
print(pairs.get(1)) # interestingly this outputs "False"

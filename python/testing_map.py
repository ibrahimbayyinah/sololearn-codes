def rwb(x):
    return x.replace(x, 'b')

text = "hello there mate"
result = tuple(map(rwb, text))
b = "".join(result)
print(len(result) == len(b))

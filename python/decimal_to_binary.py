# INCOMPLETE

def bits(x):
    for i in range(x-1, -1, -1):
        yield 2**i

a = list(bits(8))
#a = [2**i for i in range(7,-1,-1)]
#print(a)

maxValue = sum(a)

if maxValue 

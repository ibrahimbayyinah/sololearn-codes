n = int(input("Enter a number that you want to calculate the factorial of:\n"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("the factorial of {n}: {x}".format(n=n, x=fact))

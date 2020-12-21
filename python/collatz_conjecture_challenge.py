def f(numb):
    if numb % 2 == 0:
        return numb // 2
    else:
        return (numb * 3) + 1

num = int(input())
print(f"Starting point: x = {num}")

iterations = 0

while num != 1:
    num = f(num)
    print(num)
    iterations += 1

print(f"Took {iterations} iterations for x to converge to 1")


#(lambda x: x // 2 if x % 2 == 0 else x * 3 + 1)(int(input()))

# This code needs editing.

def fac(n): # This function takes as input an integer n and returns the factorial of that integer
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result
    
def trail_zeros(n): # This function takes an integer n as input and returns the number of trailing zeros in the factorial of n 
    n_str = str(fac(n))
    zeros_count = 0
    if n_str[-1] == '0':
        for digit in n_str[::-1]:
            if digit == '0':
                zeros_count += 1
            else:
                return zeros_count
    return zeros_count


### TESTING ###    
print(trail_zeros(0))
print(trail_zeros(5))
print(trail_zeros(10))
print(trail_zeros(20))
print(trail_zeros(30))
print(trail_zeros(40))

'''
This program calculates the real roots of a quadratic equation.


Please input the coefficients of the quadratic equation as the example below:

If you want to calculate the roots of the following quadratic equation: 2x^2 + 7x + 4 = 0, then you need to input the following: 2, 7, 4

Created by ibrahimbayyinah
'''

import math
coefficients_str = input("Enter the 3 coefficients: ")
coefficients = coefficients_str.split(sep=",")
print(coefficients, "\n")

try:
    a = float(coefficients[0])
    b = float(coefficients[1])
    c = float(coefficients[2])
    d = b**2 - 4 * a * c
    
    print("The quadratic equation that you entered is: {0}x^2 + {1}x + {2} = 0".format(int(a), int(b), int(c)))


    if d >= 0:
        root1 = (- b - math.sqrt(d)) / (2 * a)
        root1 = round(root1, 3)
        root2 = (- b + math.sqrt(d)) / (2 * a)
        root2 = round(root2, 3)
        print("Answer =", {root1, root2})
    else:
        print("This equation has no real roots. Maybe soon I will create a program to calculate complex roots.")
except:
    print("Invalid input! Please enter the coefficients of the quadratic equation as the example below:\nIf you want to calculate the roots of the following quadratic equation: 2x^2 + 7x + 4 = 0, then you need to input the following: 2, 7, 4")
finally:
    print("\nLike this code to motivate me to improve it! Suggestions/feedback is always welcome and appreciated.")

# INCOMPLETE

import math

class QuadEq:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def roots(self):
        d = self.b**2 - 4 * self.a * self.c
        if d < 0:
            print("This quadratic equation has no real roots.")
        elif d == 0:
            root = - self.b / (2 * self.a)
            return root
        else:
            root1 = (- self.b - math.sqrt(d)) / (2 * a)
            root2 = (- self.b + math.sqrt(d)) / (2 * a)
            return root1, root2

qe = input("Enter the coefficients of the quadratic equation in the correct order: ")
bla = QuadEq(qe)
print(bla.roots())

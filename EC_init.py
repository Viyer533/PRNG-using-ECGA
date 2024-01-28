from mod import Mod
from sympy import mod_inverse, Symbol

class EC:
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    # def EC_check(self, x, y):
    #     return y**2 == ((x**3 + self.a * x + self.b) % self.p)

    def EC_double(self, G):
        x1, y1 = G
        s1 = 2 * y1
        denom = mod_inverse(s1, self.p)
        numer = ((3 * x1**2) + self.a)
        lambda_ = (numer * denom) % self.p
        # x_new = (lambda_**2 - 2 * x1) % self.p
        # Calculate y3
        # y_new = (lambda_ * (x1 - x_new) - y1) % self.p
        return lambda_
    
    def EC_add(self, G0):
        # print(f"p: {self.p}, a: {self.a}, b: {self.b}")
        lambda_ = self.EC_double(G0)
        x1, y1 = G0
        s1 = lambda_**2
        s2 = 2 * x1
        s3 = s1 - s2
        x3 = s3 % self.p
        y3 = (lambda_ * (x1 - x3) - y1) % self.p
        # else:
        #     print(f"({x3},{y3}) does not exist on the EC\n")
        #     return None
        G3 = (x3, y3)
        return G3

    def gen_points(self, n, G0, gen_points_arr):
        for i in range(0,n):
            G0 = self.EC_add(G0)
            if G0==None:
                return gen_points_arr
            print(f"GO: {G0} for iter {i} \n")
            gen_points_arr.append(G0)
        return gen_points_arr

    # Add code for binary ops on gen_points_arr
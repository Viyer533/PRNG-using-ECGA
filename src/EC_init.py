from utils import get_params
from sympy import mod_inverse, Symbol

class EC:
    def __init__(self):
        params = get_params()
        self.p, self.a, self.b, self.G0 = params["p"], params["a"], params["b"], params["G0"]

    # def EC_check(self, x, y):
    #     return y**2 == ((x**3 + self.a * x + self.b) % self.p)

    def ec_double(self, G):
        x1, y1 = G
        s1 = 2 * y1
        denom = mod_inverse(s1, self.p)
        numer = ((3 * x1**2) + self.a)
        lambda_ = (numer * denom) % self.p

        return lambda_
    
    def ec_add(self, G0):
        lambda_ = self.ec_double(G0)
        x1, y1 = G0
        s1 = lambda_**2
        s2 = 2 * x1
        s3 = s1 - s2
        x3 = s3 % self.p
        y3 = (lambda_ * (x1 - x3) - y1) % self.p

        G3 = (x3, y3)
        return G3

    def gen_points(self, n):
        gen_points_arr = []
        G0 = self.G0
        for i in range(0,n):
            G0 = self.ec_add(G0)
            gen_points_arr.append(G0)
        return gen_points_arr

    # Add code for binary ops on gen_points_arr
inp = get_params()
ec = EC()
gen_points = ec.gen_points(5)
print(gen_points)
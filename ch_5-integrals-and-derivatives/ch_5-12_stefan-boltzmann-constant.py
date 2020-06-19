from numpy import exp
from gaussxw import gaussxwab


def f(z):
    return (z / (1 - z)) ** 3 / (exp(z / (1 - z)) - 1) * 1 / (1 - z) ** 2


# integrand is pretty smooth, so can use gaussian quadrature
n_points = 50
x, w = gaussxwab(n_points, 0, 1)
integral = 0.0

for k in range(1, n_points):
    integral += w[k] * f(x[k])

print(integral)

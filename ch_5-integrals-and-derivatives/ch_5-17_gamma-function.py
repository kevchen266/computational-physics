from numpy import exp, log
from gaussxw import gaussxwab

# for change of variables z = x / (c + x), x = c gives z = 1/2
# thus since the max of x^(a-1) e^-x occurs at a-1, choosing c = a-1 puts the peak of the integrand at z = 1/2
# we use gaussian quadrature with 100 points
N = 100
x, w = gaussxwab(N, 0, 1)


def gamma(a):
    c = a - 1

    def integrand(z):
        return c * exp(c * log((c * z) / (1 - z)) - (c * z) / (1 - z)) / (1 - z) ** 2

    integral = 0
    for k in range(N):
        integral += w[k] * integrand(x[k])

    return integral


print(gamma(3 / 2))  # exact value is sqrt(pi)/2
print(gamma(10))  # equals 9! = 362880

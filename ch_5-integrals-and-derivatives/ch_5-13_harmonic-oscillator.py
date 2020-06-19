from numpy import linspace, sqrt, pi, exp
from math import factorial
from gaussxw import gaussxwab
from pylab import plot, show, legend, xlabel, title


def H(n, x):
    """
    computes the n-th Hermite polynomial using a linear iterative procedure
    :param n: integer
    :param x: value of x
    :return: value of H_n(x)
    """

    def H_iter(a, b, count):
        if count == 0:
            return b
        else:
            return H_iter(2 * x * a - 2 * (count - 1) * b, a, count - 1)

    return H_iter(2 * x, 1, n)


# plot H for n = 0 - 3, x between -4, 4
x_values = linspace(-4, 4, 100)
H0values = []
H1values = []
H2values = []
H3values = []
for k in range(100):
    H0values.append(H(0, x_values[k]))
    H1values.append(H(1, x_values[k]))
    H2values.append(H(2, x_values[k]))
    H3values.append(H(3, x_values[k]))

plot(x_values, H0values)
plot(x_values, H1values)
plot(x_values, H2values)
plot(x_values, H3values)
xlabel("x")
legend(("$H_0$", "$H_1$", "$H_2$", "$H_3$"))
show()


def psi(n, x):
    return 1 / sqrt(2 ** n * factorial(n) * sqrt(pi)) * exp(- x ** 2 / 2) * H(n, x)


x_values = linspace(-10, 10, 500)
H30values = []
for k in range(500):
    H30values.append(psi(30, x_values[k]))
plot(x_values, H30values)
xlabel("x")
title("$H_{30}$")
show()


def rms_integrand(z):
    def x(z):
        return z / (1 - z)

    return x(z) ** 2 * abs(psi(5, x(z))) ** 2 * (1 / (1 - z) ** 2)


integral = 0.0
N = 100
x, w = gaussxwab(N, 0, 1)
for k in range(N):
    integral += w[k] * rms_integrand(x[k])
print(sqrt(2 * integral))

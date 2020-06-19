from numpy import linspace, tanh, cosh
from pylab import plot, show, xlabel, title


def f(x):
    return 1 + 0.5 * tanh(2 * x)


def df_dx(x):
    """
    calculate df/dx using central difference method
    :param x: float
    :return: float
    """
    h = 10 ** -5  # step size
    return (f(x + 0.5 * h) - f(x - 0.5 * h)) / h


def g(x):
    """analytic derivative of f(x) above is sech^2"""
    return 1 / cosh(2 * x) ** 2


x_vals = linspace(-2, 2, 100)
df_vals = list(map(df_dx, x_vals))
g_vals = list(map(g, x_vals))

plot(x_vals, df_vals, 'o')
plot(x_vals, g_vals)
xlabel('x')
title(r"$\sech^2(x)$")
show()

from numpy import sqrt, cos, pi, sin, linspace
from pylab import plot, show, xlabel, ylabel
from gaussxw import gaussxwab


def integrator(f, a, b, N):
    """
    integrates f from a to b using Gaussian quadrature with N points, requires gaussxwab
    :param f: 1d function
    :param a: lower bound of domain
    :param b: upper bound of domain
    :param N: number of points
    :return:  floating value of integral
    """
    x, w = gaussxwab(N, a, b)
    integral = 0.0
    for k in range(N):
        integral += w[k] * f(x[k])

    return integral


def I(x, wavelength, z):
    """

    :param x: x in meters
    :param wavelength: in meters
    :param z: in meters
    :return: value of I / I0
    """
    u = x * sqrt(2 / (wavelength * z))
    N = 50  # number of integration points

    def c(u):
        def f(x):
            return cos(0.5 * pi * x ** 2)

        return integrator(f, 0, u, N)

    def s(u):
        def g(x):
            return sin(0.5 * pi * x ** 2)

        return integrator(g, 0, u, N)

    return 1 / 8 * ((2 * c(u) + 1) ** 2 + (2 * s(u) + 1) ** 2)


# plot I/I0 for x between -5 and 5 m, wavelength = 1, z = 3 m
x_values = linspace(-5, 5, 100)
y_values = []
wavelength = 1
z = 3
for k in range(100):
    y_values.append(I(x_values[k], wavelength, z))

plot(x_values, y_values)
xlabel('x (m)')
ylabel('I/I0')
show()

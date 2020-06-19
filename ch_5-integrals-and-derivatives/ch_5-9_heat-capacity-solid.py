from numpy import exp, linspace
from gaussxw import gaussxwab
from pylab import plot, show, xlim, xlabel, ylabel


def c_v(T):
    c = 7.48279  # = 9V * rho * k_B in SI units
    theta_d = 428  # in K

    def f(x):
        return x**4 * exp(x) / (exp(x) - 1)**2

    # perform the integration using Gaussian quadrature
    n_points = 50
    x, w = gaussxwab(n_points, 0, theta_d / T)
    integral = 0.0
    for k in range(n_points):
        integral += w[k] * f(x[k])

    return c * (T / theta_d) ** 3 * integral


T = linspace(5, 500, 99)
C = list(map(c_v, T))
plot(T, C, 'o')
xlim(5, 500)
xlabel('T (K)')
ylabel('$C_V$ (J/K)')
show()

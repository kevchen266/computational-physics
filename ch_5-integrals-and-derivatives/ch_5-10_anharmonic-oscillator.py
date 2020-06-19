from numpy import sqrt, linspace
from gaussxw import gaussxwab
from pylab import plot, show, xlabel, ylabel

m = 1
n_points = 20


def T(a):
    def f(x):
        def v(y):
            return y ** 4

        return 1 / sqrt(v(a) - v(x))

    x, w = gaussxwab(n_points, 0, a)
    integral = 0.0
    for k in range(n_points):
        integral += w[k] * f(x[k])

    return sqrt(8) * integral


a = linspace(0.1, 2, 20)
periods = list(map(T, a))
plot(a, periods, 'o')
xlabel('a (m)')
ylabel('T (s)')
show()

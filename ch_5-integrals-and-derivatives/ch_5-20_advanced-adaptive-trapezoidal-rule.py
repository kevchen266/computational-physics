from numpy import sin, log
from pylab import plot, show, xlabel


def f(x):
    if x == 0:
        return 1
    else:
        return sin(x) ** 2 / x ** 2


def g(x):
    return log(10 * x + 1)


integration_slices = []


def integral(f, a, b, error):
    delta = error / (b - a)  # target accuracy per unit interval

    def step(x1, x2, f1, f2):
        # calculates estimates of the integral from x1 to x2 with one and two slices, and the est. error
        h = x2 - x1
        midpoint = 0.5 * (x2 + x1)
        f_mid = f(midpoint)
        I1 = h * 0.5 * (f1 + f2)
        I2 = 0.5 * I1 + 0.5 * h * f_mid
        if abs(1 / 3 * (I2 - I1)) < h * delta:
            integration_slices.append(x1)
            integration_slices.append(x2)
            return 1 / 6 * h * (f1 + 4 * f_mid + f2)
        else:
            return step(x1, midpoint, f1, f_mid) + step(midpoint, x2, f_mid, f2)

    return step(a, b, f(a), f(b))


print(integral(f, 0, 10, 10 ** -4))

vals = list(map(f, integration_slices))
plot(integration_slices, vals, 'o')
xlabel("x")
show()

from numpy import exp, linspace, array
from pylab import plot, show, xlabel, ylabel


def f(t):
    return exp(-t**2)


# integrate using simpson's method
def e(x):
    a = 0
    b = x
    n_slices = 1000
    h = (b - a) / n_slices
    odd_sum = 0
    for k in range(1, n_slices, 2):
        odd_sum += f(a + k*h)

    even_sum = 0
    for k in range(2, n_slices, 2):
        even_sum += f(a + k * h)

    return 1 / 3 * h * (f(a) + f(b) + 4 * odd_sum + 2 * even_sum)


# make a plot of E(x)
points = linspace(0, 3, 100)
values = array(list(map(e, points)))

plot(points, values)
xlabel("x")
ylabel("E(x)")
show()

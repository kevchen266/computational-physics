from numpy import array, empty, abs
from pylab import plot, show, xlabel, ylabel, xscale, title


def f(x):
    return x * (x - 1)


deltas = array([10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14])
exact_ans = 1
ans = empty(deltas.size)

for j in range(len(deltas)):
    ans[j] = abs((f(1 + deltas[j]) - f(1)) / deltas[j] - exact_ans)


plot(deltas, ans, 'o')
xscale('log')
xlabel("$\delta$")
ylabel("Magnitude of absolute error")
title("Numerical error of derivative of x(x-1) at x=1")
show()
# for smaller and smaller delta, the approximation of the limit gets better, but at some point it gets worse due to
# numerical error arising from the difference of numbers that are nearly equal.

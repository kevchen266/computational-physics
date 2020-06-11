from numpy import zeros, arange
from pylab import plot, show, xlabel, ylabel

# Constants
g = 9.81  # m/s^2
t_0 = 0
t_f = 10  # seconds
N = 100  # grid points
h = t_f / N
c = h ** 2 / 2 * g
epsilon = 10 ** -6

# main loop
x = zeros(N + 1, float)
max_error = 2 * epsilon
while max_error > epsilon:
    # reset max_error after each update
    max_error = 0.0
    for i in range(1, N):
        old_x = x[i]
        x[i] = c + (x[i - 1] + x[i + 1]) / 2
        max_error = max(max_error, abs(old_x - x[i]))

t_points = arange(0, 10.1, 0.1)
plot(t_points, x)
xlabel("t (s)")
ylabel("y (m)")
show()

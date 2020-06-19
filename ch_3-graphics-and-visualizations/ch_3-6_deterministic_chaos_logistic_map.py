from numpy import arange, zeros
from pylab import plot, show, xlabel, ylabel, title

n_iterations = 1000
r_values = arange(1, 4, 0.001)
x_array = zeros(r_values.size, float) + 0.5

# iterate to settle down to a fixed point or limit cycle if it's going to
for i in range(0, n_iterations):
    x_array = r_values * x_array * (1 - x_array)

# get one set of branches
for i in range(0, n_iterations + 1):
    x_array = r_values * x_array * (1 - x_array)
plot(r_values, x_array, '.', color="k")

# get another set of branches
for i in range(0, n_iterations + 1):
    x_array = r_values * x_array * (1 - x_array)
plot(r_values, x_array, '.', color="k")

for i in range(0, n_iterations + 1):
    x_array = r_values * x_array * (1 - x_array)
plot(r_values, x_array, '.', color="k")

for i in range(0, n_iterations + 1):
    x_array = r_values * x_array * (1 - x_array)
plot(r_values, x_array, '.', color="k")

plot(r_values, x_array, '.', color="k")
xlabel("r")
ylabel("x")
title("Feigenbaum plot")
show()

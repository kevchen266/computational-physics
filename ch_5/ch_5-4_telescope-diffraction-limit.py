from numpy import cos, sin, pi, linspace, sqrt, empty
from pylab import plot, legend, xlabel, show, imshow, hot, close


def J(m, x):
    def f(m, x, theta):
        return cos(m * theta - x * sin(theta))

    N = 1000
    a = 0
    b = pi
    h = (b - a) / N

    odd_sum = 0
    for k in range(1, N, 2):
        odd_sum += f(m, x, a + k * h)

    even_sum = 0
    for k in range(1, N, 2):
        even_sum += f(m, x, a + k * h)

    return 1 / pi * 1 / 3 * h * (f(m, x, a) + f(m, x, b) + 4 * odd_sum + 2 * even_sum)


# Plot J0, J1, J2
x_points = linspace(0, 20, 100)
J0 = []
J1 = []
J2 = []
for x in x_points:
    J0.append(J(0, x))
    J1.append(J(1, x))
    J2.append(J(2, x))

plot(x_points, J0, "g")
plot(x_points, J1, "b")
plot(x_points, J2, "r")
legend(("$J_0$", "$J_1$", "$J_2$"))
xlabel("x")
show()
close()


# Part b
def r(x, y):
    return sqrt(x**2 + y**2)


def I(r):
    if r == 0:
        return 1/4

    Lambda = 0.5 # in micrometers
    kr = 2 * pi / Lambda * r
    return (J(1, kr)/ kr)**2


side = 2  # length in micrometers
points = 200  # number of grid points in each direction
spacing = side / points

# Calculate the position of the center
x_center = side / 2
y_center = side / 2

# Make an empty array to store values
intensities = empty([points, points], float)

# Calculate the values in the array
for i in range(points):
    y = spacing * i
    for j in range(points):
        x = spacing * j
        dist = r(x - x_center, y - y_center)
        intensities[i, j] = I(dist)

imshow(intensities, origin="lower", extent=[0, side, 0, side], vmax=0.01)
hot()
show()

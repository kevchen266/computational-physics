from scipy import zeros, sin, pi, empty, arange
from pylab import plot, show, xlabel, ylabel

# Constants
# Note need to ensure h < a^2 / 2 * D to ensure numerical stability
D = 0.1  # diffusion constant in m^2 / day
x_0 = 0
x_f = 20  # final depth in m
t_0 = 0
t_f = 10 * 365  # 10 years in days
N = 100  # number of spatial grid points
a = x_f / N
h = (t_f - t_0) / 100000  # time step size in days
c = h * D / (a) ** 2
epsilon = h / 10000


print(a ** 2 / (2 * D))
print('h = ', h)

t1 = 3285  # 9 years in days
t2 = 3376.25
t3 = 3467.5
t4 = 3558.75


def T(t):
    return 10 + 12 * sin(2 * pi * t / 365)


# Create arrays
temp = zeros([N + 1], float)
temp = temp + 10
temp[N] = 11  # Celsius
temp_1 = empty([N + 1], float)
temp_1[0] = T(0)
temp_1[N] = 11

# Loop
t = t_0
while t < t_f:
    temp[0] = T(t)
    temp_1[1: N] = temp[1: N] + c * (temp[0: N - 1] + temp[2: N + 1] - 2 * temp[1: N])
    temp, temp_1 = temp_1, temp
    t += h

    # Make plots at desired times
    if abs(t - t1) < epsilon:
        plot(temp, 'b')
    elif abs(t - t2) < epsilon:
        plot(temp, 'g')
    elif abs(t - t3) < epsilon:
        plot(temp, 'r')
    elif abs(t - t4) < epsilon:
        plot(temp, color='orange')

xlabel("x")
ylabel("T")
show()
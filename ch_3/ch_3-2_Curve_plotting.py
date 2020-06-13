from numpy import linspace, cos, sin, pi, exp
from pylab import plot, show, xlabel, ylabel, title

theta = linspace(0, 2 * pi, 50)
x = 2 * cos(theta) + cos(2 * theta)
y = 2 * sin(theta) - sin(2 * theta)
plot(x, y)
xlabel("x")
ylabel("y")
title("Deltoid")
show()

# Galilean spiral
theta_galilean = linspace(0, 10 * pi, 1000)
r = theta_galilean ** 2
x = r * cos(theta_galilean)
y = r * sin(theta_galilean)
plot(x, y)
xlabel("x")
ylabel("y")
title("Galilean spiral")
show()

# Fey's function
theta_fey = linspace(0, 24 * pi, 1000)
r = exp(cos(theta_fey)) - 2 * cos(4 * theta_fey) + sin(theta_fey / 12) ** 5
x = r * cos(theta_fey)
y = r * sin(theta_fey)
plot(x, y)
title("Fey's function")
show()

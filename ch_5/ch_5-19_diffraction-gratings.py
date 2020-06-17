from numpy import pi, sqrt, exp, linspace, sin, empty
from pylab import plot, show, imshow, gray, xlabel, ylabel

focal_len = 1  # in m
screen_width = 0.1  # in m
wavelength = 0.5  # in um (micrometers)
slit_sep = 20  # in um
num_slits = 10
grating_width = slit_sep * num_slits


def q(u):
    alpha = pi / slit_sep
    return sin(alpha * u) ** 2


def I(x):
    # The integrand is highly oscillatory, so let's just use the trapezoidal rule
    # note we've scaled u in terms of um
    def integrand(u):
        return sqrt(q(u)) * exp(2j * pi * x * u / (wavelength * focal_len))

    N = 1000  # num of integration slices
    h = grating_width / N  # step size
    integral = h * 0.5 * (integrand(- grating_width / 2) + integrand(grating_width / 2))
    for k in range(1, N, 2):
        integral += integrand(-grating_width / 2 + k * h)

    return 10 ** -12 * abs(integral) ** 2


x_vals = linspace(-.05, .05, 500)
I_vals = list(map(I, x_vals))

plot(x_vals, I_vals, 'o')
xlabel("x (m)")
ylabel("$I(x)$")
show()
#
I_array = empty([100, 500], float)
for k in range(100):
    I_array[k, :] = I_vals
imshow(I_array)
gray()
show()

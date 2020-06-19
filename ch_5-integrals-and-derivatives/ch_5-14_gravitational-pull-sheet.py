from numpy import linspace
from gaussxw import gaussxwab
from pylab import plot, show, xlabel, ylabel

G = 6.674 * 10 ** -11  # gravitational constant in SI units
sigma = 100  # mass density in SI units
N = 100  # number of points in each direction for double Gaussian quadrature
r, w = gaussxwab(N, -5, 5)


def Fz(z):
    def integrand(x, y, z):
        return 1 / (x ** 2 + y ** 2 + z ** 2) ** 3 / 2

    integral = 0
    for i in range(N):
        for j in range(N):
            integral += w[i] * w[j] * z * integrand(r[i], r[j], z)

    return G * sigma * integral


z_values = linspace(0, 10, 100)
F_z_values = list(map(Fz, z_values))

plot(z_values, F_z_values, 'o')
xlabel('z (m)')
ylabel('Fz (N)')
show()
# The force seems to drop to zero for small values of z because the integrand becomes very small for points
# far from x,y = 0, and we don't have enough points near (0,0) when calculating the integral

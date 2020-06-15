from numpy import loadtxt, dot, empty
from pylab import plot, show, xlabel, ylabel

data = loadtxt('../cpresources/millikan.txt', float)
x = data[:, 0]
y = data[:, 1]
N = x.size

Ex = 1/N * sum(x)
Ey = 1/N * sum(y)
Exx = 1/N * sum(x**2)
Exy = 1/N * dot(x, y)
m = (Exy - Ex * Ey)/(Exx - Ex**2)
c = (Exx * Ey - Ex * Exy)/(Exx - Ex**2)

new_y = empty(N, float)
for i in range(0, N):
    new_y[i] = m * x[i] + c

print(f"estimated value for h = {(m * 1.602e-19):.4} J s")

plot(x, y, 'ko')
plot(x, new_y, 'k')
xlabel(r"$\nu$ (Hz)")
ylabel("Voltage (V)")
show()

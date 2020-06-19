from numpy import loadtxt, array
from pylab import plot, show, xlabel, legend

data = loadtxt("../cpresources/velocities.txt", float)
times = data[:, 0]
velocities = data[:, 1]


def x(t):
    if t == 0:
        return 0
    a = times[0]
    b = times[int(t)]
    h = (b - a) / t

    return h*(0.5*velocities[0] + 0.5 * velocities[int(t)] + sum(velocities[1: int(t)]))


positions = array(list(map(x, times)), float)

plot(times, positions)
plot(times, velocities)
xlabel("t")
legend(("position", "velocity"))
show()

from numpy import zeros, random, empty, sum, exp, copy
from pylab import imshow, show, colorbar, plot, xlabel, ylabel, title
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rng = random.default_rng()  # random number generator
N_side = 100


def get_energy(J, system):
    row_sum = zeros([1, N_side], int)
    for i in range(0, N_side - 1):
        row_sum += -J * system[i, :] * system[i + 1, :]

    column_sum = zeros(N_side, int)
    for i in range(0, N_side - 1):
        column_sum += -J * system[:, i] * system[:, i + 1]

    return sum(row_sum[0]) + sum(column_sum)


def get_magnetization(system):
    return sum(system)


def random_initial_state():
    result = empty([N_side, N_side], dtype=int)

    def random_state():
        x = rng.integers(0, 1, endpoint=True)
        if x == 0:
            return -1
        else:
            return 1

    for i in range(0, N_side):
        for j in range(0, N_side):
            result[i, j] = random_state()
    return result


def should_accept_move(beta, delta_E):
    prob_accept = 1 if delta_E <= 0 else exp(- beta * delta_E)
    return True if rng.random() < prob_accept else False


def flip_spin(spin):
    return 1 if spin == -1 else -1


def contribution_to_energy(J, system, i, j, spin):
    contribution = 0
    if i == 0:
        contribution += -J * spin * system[i + 1, j]
    elif i == len(system) - 1:
        contribution += -J * spin * system[i - 1, j]
    else:
        contribution += -J * spin * (system[i - 1, j] + system[i + 1, j])
    if j == 0:
        contribution += -J * spin * system[i, j + 1]
    elif j == len(system) - 1:
        contribution += -J * spin * system[i, j - 1]
    else:
        contribution += -J * spin * (system[i, j - 1] + system[i, j + 1])

    return contribution


N_MC_steps = 10000000
beta = 0.440687
J = 1

state = random_initial_state()
initial_state = copy(state)
states = [initial_state]
old_energy = get_energy(J, state)
magnetization = [get_magnetization(state) / (N_side ** 2)]

for step in range(0, N_MC_steps):
    i = rng.integers(0, N_side)
    j = rng.integers(0, N_side)
    old_contribution = contribution_to_energy(J, state, i, j, state[i, j])
    new_contribution = contribution_to_energy(J, state, i, j, flip_spin(state[i, j]))
    if should_accept_move(beta, new_contribution - old_contribution):
        state[i, j] = flip_spin(state[i, j])
        old_energy += new_contribution - old_contribution
    magnetization.append(get_magnetization(state) / (N_side ** 2))

plot(magnetization)
xlabel("time step")
ylabel("m")
title(fr"Average magnetization m per spin, $\beta={beta}, J={J}, k_B=1$")
show()
plt.close()

cmap = colors.ListedColormap(['#56b4e9', '#d55e00'])
bounds = [-1, 0, 1]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig = plt.figure()
# plt = imshow(states[0], norm=norm, cmap=cmap, extent=[1, N_side, 1, N_side], animated=True)
# colorbar(cmap=cmap, ticks=[-1, 1], norm=norm, boundaries=bounds)


# def update_fig(i):
#     if i < N_MC_steps:
#         i += 1
#     else:
#         print('end')
#     plt.set_array(states[i])
#     return plt,

# run animation
# ani = animation.FuncAnimation(fig, update_fig, blit=True, interval=1)
# show()

plt.subplot(1, 2, 1)
imshow(initial_state, norm=norm, cmap=cmap, extent=[1, N_side, 1, N_side], animated=True)
# colorbar(cmap=cmap, ticks=[-1, 1], norm=norm, boundaries=bounds)
title(f"Initial state of system")
# show()
# plt.close()

plt.subplot(1, 2, 2)
imshow(state, norm=norm, cmap=cmap, extent=[1, N_side, 1, N_side], animated=True)
title(f"System after {N_MC_steps:,} steps")
show()
plt.close()

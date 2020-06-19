from numpy import full, linspace, meshgrid, zeros, log
from pylab import imshow, hot, colorbar, show

N_points = 450
num_iterations = 150
grid = full([N_points, N_points], num_iterations, int)

cx, cy = meshgrid(linspace(-2, 2, N_points), linspace(-2, 2, N_points))

z = zeros([N_points, N_points], complex)

for n in range(0, num_iterations):
    z = z**2 + cx + cy * 1j
    for i in range(0, N_points):
        for j in range(0, N_points):
            if abs(z[i, j]) > 2:
                grid[i, j] = n + 1

# density plot colored based on the number of iterations to reach
# |z| > 2
imshow(grid, origin='lower', extent=[-2, 2, -2, 2])
hot()
colorbar()
show()

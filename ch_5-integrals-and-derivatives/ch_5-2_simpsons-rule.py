def g(x):
    return x**4 - 2 * x + 1


def integral(f, a, b, n_slices):
    h = (b - a) / n_slices
    odd_sum = 0
    for k in range(1, n_slices, 2):
        odd_sum += f(a + k * h)

    even_sum = 0
    for k in range(2, n_slices, 2):
        even_sum += f(a + k * h)

    return 1 / 3 * h * (f(a) + f(b) + 4 * odd_sum + 2 * even_sum)


print(integral(g, 0, 2, 10))
print(integral(g, 0, 2, 100))
print(integral(g, 0, 2, 1000))

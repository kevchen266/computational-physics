from numpy import arange


def f(x):
    return x**4 - 2 * x + 1


N1 = 10
N2 = 2 * N1
a = 0
b = 2
h1 = (b - a) / N1
h2 = (b - a) / N2

f_values = sum(list(map(f, arange(a + h1, b, h1))))
nested_f_values = sum(list(map(f, arange(a + h2, b, h1))))

I1 = h1 * (0.5 * f(a) + 0.5 * f(b) + f_values)
I2 = h2 * (0.5 * f(a) + 0.5 * f(b) + f_values + nested_f_values)
epsilon = 1/3 * (I2 - I1)
print(I1)
print(I2)
print("error is approximately", epsilon)
print(I2 + epsilon)
# error estimate is good to only h^2

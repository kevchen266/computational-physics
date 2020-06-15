def factorial_int(n):
    prod = 1
    for k in range(n, 0, -1):
        prod *= k
    return prod


def factorial_float(n):
    prod = 1.0
    for k in range(n, 0, -1):
        prod *= k
    return prod


print(factorial_int(200))
print(float(200))


# for the floating point version, 200! overflows, i.e. is larger than the largest possible float,
# but integer calculations are done to arbitrary precision

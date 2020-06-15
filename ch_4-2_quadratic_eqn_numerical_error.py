from numpy import sqrt


def quadratic(a, b, c):
    """
    prints out both solutions of the associated quadratic equation
    using both forms of the standard formula for the roots

    :param a: quadratic coefficient
    :param b: linear coefficient
    :param c: constant term
    :return: None
    """

    print('Solution one: ', (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    print('Solution two: ', (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    print('Alternative form one:', (2 * c) / (-b - sqrt(b ** 2 - 4 * a * c)))
    print('Alternative form one:', (2 * c) / (-b + sqrt(b ** 2 - 4 * a * c)))


quadratic(0.001, 1000, 0.001)


def quadratic_roots(a, b, c):
    """
    Returns the roots of a quadratic equation, in order of larger to smaller magnitude.
    We should choose the form of the solution that avoids the difference of two nearly equal numbers.
    This depends on the values of -b and the square root of the discriminant b**2 - 4*a*c

    :param a: leading coefficient
    :param b: linear coefficient
    :param c: constant term
    :return: (number, number)
    """
    tolerance = 10*-3
    discriminant = sqrt(b ** 2 - 4 * a * c)
    if abs(discriminant + b) < tolerance:
        return (2 * c) / (-b + discriminant), (-b + discriminant) / (2 * a)
    else:
        return (-b - discriminant) / (2 * a), (2 * c) / (-b - discriminant)


print(quadratic_roots(0.001, 1000, 0.001))

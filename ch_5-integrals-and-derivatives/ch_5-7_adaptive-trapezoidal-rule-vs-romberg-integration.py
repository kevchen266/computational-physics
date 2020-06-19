from numpy import arange, sin, sqrt


# part a
def adap_trap(f, a, b, n, prev_estimate, error):
    n = 2 * n
    h = (b - a) / n
    integral = 0.5 * prev_estimate + h * sum(list(map(f, arange(a + h, b, 2 * h))))
    epsilon = 1 / 3 * (integral - prev_estimate)
    print('number of slices = ', n)
    print("integral estimate is", integral)
    print('error = ', epsilon)
    if abs(epsilon) < error:
        return integral
    else:
        return adap_trap(f, a, b, n, integral, error)


def f(x):
    return sin(sqrt(100 * x)) ** 2


# print(adap_trap(f, 0, 1, 1, 0.5 * (f(1) - f(0)), .000001))


# part b


def adap_trap_step(f, a, b, n, prev_estimate):
    n = 2 * n
    h = (b - a) / n
    integral = 0.5 * prev_estimate + h * sum(list(map(f, arange(a + h, b, 2 * h))))
    return integral


def romberg(f, a, b, error):
    # initial estimate of integral with N=2
    R11 = (b - a) / 2 * (0.5 * f(a) + 0.5 * f(b) + f(a + (b - a) / 2))
    # keep a list of the romberg estimates
    R_list = [R11, adap_trap_step(f, a, b, 2, R11)]

    def Rij(i, m):
        """
        returns the linear index of Rij corresponding to i, m given by sum_{j=0}^{i-1} + m - 1
        :param i: int - ith trapezoidal rule step
        :param m: int - mth extrapolation
        :return: float
        """
        return R_list[int(1 / 2 * i * (i - 1) + m - 1)]  #

    def romberg_step(i, m):
        """
        returns R_i,m such that error estimate is less than given error
        :param i: int - ith trapezoidal rule step
        :param m: int - mth extrapolation
        :return: float
        """
        if m == 1:
            # if m = 1, then need to compute the next nested trapezoidal rule estimate
            print('i = ', i)
            print('m = ', m)
            R_list.append(adap_trap_step(f, a, b, 2 ** (i - 1), Rij(i - 1, 1)))
            epsilon = 1 / 3 * (Rij(i, 1) - Rij(i - 1, 1))
            print('current estimate =', Rij(i, m))
            print('epsilon = ', epsilon)
            if abs(epsilon) < error:
                return Rij(i, m)
            else:
                return romberg_step(i, m + 1)
        else:
            print('i = ', i)
            print('m = ', m)
            epsilon = 1 / (4 ** (m - 1) - 1) * (Rij(i, m - 1) - Rij(i - 1, m - 1))
            print('epsilon = ', epsilon)
            R_list.append(Rij(i, m - 1) + epsilon)
            print('current estimate =', Rij(i, m))
            if abs(epsilon) < error:
                return Rij(i, m)
            else:
                if i == m:
                    return romberg_step(i + 1, 1)
                else:
                    return romberg_step(i, m + 1)

    return romberg_step(2, 2)


def g(x):
    return sin(sqrt(100 * x)) ** 2


def k(x):
    return x ** 2


print(romberg(f, 0, 1, 0.000001))

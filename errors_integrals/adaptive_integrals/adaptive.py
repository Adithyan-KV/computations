import math
import time


def main():
    f = lambda x: x**4 - 2 * x + 1
    precision_points = 10
    I_1 = integrate_using_trapezoidal_rule(f, 0, 2, 10000)
    print(I_1)
    I_2 = integrate_using_adaptive_rule(f, 0, 2, precision_points)
    print(I_2)
    I_3 = integrate_using_adaptive_rule_2(f, 0, 2, precision_points)
    print(I_3)


def integrate_using_adaptive_rule(function, lower_limit, upper_limit, precision_points):
    tolerable_error = (10)**(-precision_points)
    steps = 10
    I = integrate_using_trapezoidal_rule(
        function, lower_limit, upper_limit, steps)
    error = 1
    # keep doubling the number of steps and get new estimates untill error is
    # within the required levels
    while error > tolerable_error:
        temp = I
        steps = steps * 2
        I = integrate_using_trapezoidal_rule(
            function, lower_limit, upper_limit, steps)
        error = abs(1 / 3 * (I - temp))
    return I


def integrate_using_adaptive_rule_2(function, lower_limit, upper_limit, precision_points):
    # avoids the redundant calculations in the first one
    # we already calculate half the terms of the next iteration in every
    # iteration, that redundancy can be avoided
    tolerable_error = (10)**(-precision_points)
    steps = 10
    I = integrate_using_trapezoidal_rule(
        function, lower_limit, upper_limit, steps)
    error = 1
    while error > tolerable_error:
        steps = steps * 2
        h = (upper_limit - lower_limit) / steps
        temp = I
        additional_term = 0
        for k in range(1, steps):
            if k % 2 != 0:
                additional_term += function(lower_limit + k * h)
        I = (0.5 * I) + (h * additional_term)
        error = abs((1 / 3) * (I - temp))
        # print(error)
    return I


def integrate_using_trapezoidal_rule(function, lower_limit, upper_limit, steps):
    h = (upper_limit - lower_limit) / steps
    term_1 = (1 / 2) * (function(upper_limit) + function(lower_limit))
    term_2 = 0
    for k in range(1, steps):
        term_2 += function(lower_limit + k * h)
    I = h * (term_1 + term_2)
    return I


if __name__ == "__main__":
    main()

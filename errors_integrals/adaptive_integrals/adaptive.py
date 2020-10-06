import math
import time


def main():
    f = lambda x: x**4 - 2 * x + 1
    precision_points = 12
    timestamp_1 = time.time()
    I_1 = integrate_using_trapezoidal_rule(f, 0, 2, 5242880)
    timestamp_2 = time.time()
    I_2 = integrate_using_adaptive_rule(f, 0, 2, precision_points)
    timestamp_3 = time.time()
    I_3 = integrate_using_adaptive_rule_2(f, 0, 2, precision_points)
    timestamp_4 = time.time()
    print(I_1)
    print(I_2)
    print(I_3)
    print(f'Time (conventional) : {timestamp_2-timestamp_1}')
    print(f'Time (adaptive redundant) : {timestamp_3-timestamp_2}')
    print(f'Time (adaptive non-redundant) : {timestamp_4-timestamp_3}')


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
        for k in range(1, steps, 2):
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

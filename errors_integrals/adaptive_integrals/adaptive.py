import math


def main():
    f = lambda x: x**4 - 2 * x + 1
    lower_limit = 0
    upper_limit = 2
    I = integrate_using_adaptive_method(f, lower_limit, upper_limit, 6)
    print(I)


def integrate_using_adaptive_method(function, lower_limit, upper_limit, digits_precision):
    precision_float = 1 / (10**digits_precision)
    steps = 10
    error = 1
    while error > precision_float:
        I_1 = integrate_using_trapezoidal_rule(
            function, lower_limit, upper_limit, steps)
        I_2 = integrate_using_trapezoidal_rule(
            function, lower_limit, upper_limit, 2 * steps)
        steps = steps * 2
        error = abs((1 / 3) * (I_2 - I_1))
    print(steps)
    return I_2


def integrate_using_trapezoidal_rule(function, lower_limit, upper_limit, steps):
    h = (upper_limit - lower_limit) / steps
    term_1 = (1 / 2) * (function(upper_limit) + function(lower_limit))
    term_2 = 0
    for k in range(steps):
        term_2 += function(lower_limit + k * h)
    I = h * (term_1 + term_2)
    return I


if __name__ == "__main__":
    main()

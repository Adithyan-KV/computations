import numpy as np
import matplotlib.pyplot as plt


def main():
    lower_limit = 0
    upper_limit = 2
    function = lambda x: x**4 - 2 * x + 1
    i = integrate_with_trapezoidal_rule(
        function, lower_limit, upper_limit, 100)
    print(i)


def integrate_with_trapezoidal_rule(function,
                                    lower_limit, upper_limit, iterations):
    h = (upper_limit - lower_limit) / iterations
    k = np.arange(iterations)
    # trapezoidal rule
    term_1 = 0.5 * function(upper_limit) + 0.5 * function(lower_limit)
    term_2 = 0
    for k in range(1, iterations):
        term_2 += function(lower_limit + h * k)
    I = h * (term_1 + term_2)
    return I


if __name__ == "__main__":
    main()

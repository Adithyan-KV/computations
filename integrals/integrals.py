import numpy as np
import matplotlib.pyplot as plt
import time


def main():
    lower_limit = 0
    upper_limit = 2
    function = lambda x: x**4 - 2 * x + 1
    I = integrate_with_trapezoidal_rule(
        function, lower_limit, upper_limit, 100)
    print(f'Integral: {I}')
    I2 = integrate_with_simpsons_rule(function, lower_limit, upper_limit, 100)
    print(f'Integral simpsons: {I2}')


def integrate_with_trapezoidal_rule(function,
                                    lower_limit, upper_limit, iterations):
    """Numerically integrates the function with the relevant limits using the
       trapezoidal rule.

    Args:
        function (function): The function to be integrated over
        lower_limit (float): The lower limit of integration
        upper_limit (float): The upper limit of integration
        iterations (int): The number of iterations for numerical computation,
                          the higher the number, more accurate the results.


    Returns:
        float: The value of the evaluated integral
    """
    h = (upper_limit - lower_limit) / iterations
    # trapezoidal rule https://en.wikipedia.org/wiki/Trapezoidal_rule
    term_1 = 0.5 * function(upper_limit) + 0.5 * function(lower_limit)
    term_2 = 0
    for k in range(iterations):
        term_2 += function(lower_limit + k * h)
    I = h * (term_1 + term_2)
    return I


def integrate_with_simpsons_rule(function, lower_limit, upper_limit,
                                 iterations):
    """Numerically integrates the function with the relevant limits using the
       Simpsons rule.

    Args:
        function (function): The function to be integrated over
        lower_limit (float): The lower limit of integration
        upper_limit (float): The upper limit of integration
        iterations (int): The number of iterations for numerical computation,
                          the higher the number, more accurate the results.


    Returns:
        float: The value of the evaluated integral
    """
    h = (upper_limit - lower_limit) / iterations
    term_1 = (1 / 3) * h * (function(lower_limit) + function(upper_limit))
    term_2 = 0
    for k in range(1, iterations, 2):
        term_2 += 4 * function(lower_limit + k * h)
    term_3 = 0
    for k in range(2, iterations, 2):
        term_3 += 2 * function(lower_limit + k * h)
    I = term_1 + h / 3 * (term_2 + term_3)
    return I


if __name__ == "__main__":
    main()

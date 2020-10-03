import numpy as np


def main():
    lower_limit = 0
    upper_limit = 2
    function = lambda x: x**4 - 2 * x + 1
    I_1 = integrate_with_trapezoidal_rule(
        function, lower_limit, upper_limit, 100)
    I_2 = integrate_with_trapezoidal_rule(
        function, lower_limit, upper_limit, 200)
    error_theoretical = abs((1 / 3) * (I_2 - I_1))
    error_real = abs(I_2 - 4.4)
    print(error_theoretical)
    print(error_real)
    prediction_error = abs(error_real - error_theoretical)
    print(prediction_error)


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


if __name__ == "__main__":
    main()

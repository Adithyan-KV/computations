def main():
    lower_limit = 0
    upper_limit = 2
    function = lambda x: x**4 - 2 * x + 1
    I = integrate(function, lower_limit, upper_limit, 100)
    print(I)


def integrate(function, lower_limit, upper_limit, iterations):
    """Numerically integrates the function between the limits using trapezoidal 
    rule

    Args:
        function (function object): [the function expression to be integrated]
        lower_limit (float): lower limit of integration
        upper_limit (float): upper limit of integration
        iterations (int): number of iterations over which to compute the 
                            numerical integral. generally more iterations lead
                            to more accurate results

    Returns:
        float: the computed value of the integral
    """
    h = (upper_limit - lower_limit) / iterations
    # trapezoidal rule https://en.wikipedia.org/wiki/Trapezoidal_rule
    term_1 = 0.5 * function(upper_limit) + 0.5 * function(lower_limit)
    term_2 = 0
    for k in range(1, iterations):
        term_2 += function(lower_limit + k * h)
    I = h * (term_1 + term_2)
    return I


if __name__ == "__main__":
    main()

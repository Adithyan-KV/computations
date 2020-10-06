def main():
    f = lambda x: x**4 - 2 * x + 1
    lower_limit = 0
    upper_limit = 2
    I = integrate_using_trapezoidal_rule(f, lower_limit, upper_limit, 10)
    print(I)


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

import math
import time


def main():
    lower_limit = 0
    upper_limit = 2
    f = lambda x: x**4 - 2 * x + 1
    integral = Integral(f, lower_limit, upper_limit)
    timestamp_1 = time.time()
    romberg = RombergIntegral(integral)
    timestamp_2 = time.time()
    I = integrate_using_adaptive_rule_2(f, lower_limit, upper_limit, 10)
    timestamp_3 = time.time()
    print(timestamp_2 - timestamp_1, timestamp_3 - timestamp_2)


class Integral():

    def __init__(self, function, lower_limit, upper_limit):
        self.function = function
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit


class RombergIntegral():

    def __init__(self, integral):
        self.integral = integral
        self.base_iterations = 2
        self.error = 1
        I = self.get_romberg_integral(10)
        print(I)

    def R(self, i, m):
        if m == 1:
            return self.integrate(self.integral, self.base_iterations * 2**(i - 1))
        else:
            integral_term = self.R(i, m - 1)
            error_term = (1 / ((4**(m - 1)) - 1)) * \
                (self.R(i, m - 1) - self.R(i - 1, m - 1))
            self.error = abs(error_term)
            return integral_term + error_term

    def integrate(self, integral, iterations):
        h = (self.integral.upper_limit - self.integral.lower_limit) / iterations
        term_1 = 0.5 * self.integral.function(self.integral.upper_limit) + \
            0.5 * self.integral.function(self.integral.lower_limit)
        term_2 = 0
        for k in range(1, iterations):
            term_2 += self.integral.function(self.integral.lower_limit + k * h)
        I = h * (term_1 + term_2)
        return I

    def get_romberg_integral(self, digits_precision):
        precision = 1 / (10)**digits_precision
        i = 1
        while True:
            for m in range(1, i + 1):
                integral = self.R(i, m)
                if self.error < precision:
                    return integral
            i += 1


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

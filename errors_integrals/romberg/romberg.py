def main():
    lower_limit = 0
    upper_limit = 2
    f = lambda x: x**4 - 2 * x + 1
    integral = Integral(f, lower_limit, upper_limit)
    romberg = RombergIntegral(integral)


class Integral():

    def __init__(self, function, lower_limit, upper_limit):
        self.function = function
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit


class RombergIntegral():

    def __init__(self, integral):
        self.integral = integral
        self.base_iterations = 10
        I = self.R(3, 3)
        print(I)

    def R(self, i, m):
        print(i)
        if m == 1:
            return self.integrate(self.integral, self.base_iterations * 2**(i - 1))
        else:
            integral_term = self.R(i, m - 1)
            error_term = (1 / ((4**(m - 1)) - 1)) * \
                (self.R(i, m - 1) - self.R(i - 1, m - 1))
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


if __name__ == "__main__":
    main()

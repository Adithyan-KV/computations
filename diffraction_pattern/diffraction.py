import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr


def main():
    plot_bessel_functions(4)
    # plot_diffraction_pattern(0.5)


def plot_diffraction_pattern(wavelength):
    """Generates the plot of a diffraction pattern over 1 micrometer radius for
    a wavelength 

    Args:
        wavelength (int): wavelength of light in micrometers
    """
    # side in micrometers
    side = 2
    # number of points in the grid
    points = 200
    spacing = side / points
    intensity_map = np.zeros((points, points))
    k = (2 * math.pi) / wavelength
    for x in range(points):
        for y in range(points):
            r = spacing * math.sqrt((x - (points / 2))
                                    ** 2 + (y - (points / 2))**2)
            if r == 0:
                # limiting case in bessel function
                intensity = 1 / 4
            else:
                intensity = ((bessel(1, k * r)) / (k * r))**2
            intensity_map[x, y] = intensity
        print(x)
    plt.hot()
    plt.imshow(intensity_map, vmax=0.01)
    plt.axis('off')
    # plt.colorbar()
    plt.title('Diffraction pattern')
    plt.show()


def plot_bessel_functions(n):
    """plot the first n bessel functions
    https://en.wikipedia.org/wiki/Bessel_function

    Args:
        n (int): The number of bessel functions to plot
    """
    legend_list = []
    for m in range(n):
        x_array = np.arange(0, 20, 0.1)
        y_array = []
        for x in x_array:
            y_array.append(bessel(m, x))
        plt.plot(x_array, y_array)
        legend_list.append(f'$I_{m}$')
    plt.legend(legend_list)
    plt.title("Bessel functions")
    plt.xlabel('x')
    plt.ylabel('$I(x)$')
    plt.show()


def bessel(m, x):
    """Calculates the bessel function for m and x

    Args:
        m (int): the m parameter of the bessel function
        x (int): the x parameter of the bessel function

    Returns:
        int: The value of the integral, i.e. the bessel function at x
    """
    f = lambda theta: (1 / math.pi) * math.cos(m * theta - x * math.sin(theta))
    I = integrate_with_simpsons_rule(f, 0, math.pi, 1000)
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

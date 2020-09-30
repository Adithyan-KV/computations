import math
import numpy as np
import matplotlib.pyplot as plt


def main():
    integrate(10)
    integrate(20)
    integrate(100)
    # integrate(500)
    # integrate(1000)
    # integrate(10000)
    # integrate(100000)


def integrate(number_of_points):
    """uses the riemann integral to integrate over a semicircle from -1 to 1"""
    x_value = np.linspace(-1, 1, number_of_points)
    y_value = np.sqrt(1-x_value**2)
    h = 2/number_of_points
    I = sum(h*y_value)
    I_actual = math.pi/2
    print(
        f' for n = {number_of_points} we have I = {I} with error {I-I_actual}')
    plt.bar(x_value, y_value, width=2/number_of_points)
    plot_semicircle()
    plt.show()


def plot_semicircle():
    x_value = np.linspace(-1, 1, 1000)
    y_value = np.sqrt(1-x_value**2)
    plt.plot(x_value, y_value, color='red')


if __name__ == "__main__":
    main()

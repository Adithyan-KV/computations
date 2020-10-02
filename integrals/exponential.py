import integrals
import math
import matplotlib.pyplot as plt
import numpy as np


def main():
    function = lambda x: math.exp(-(x**2))
    y_array = []
    x_array = np.arange(0, 3, 0.1)
    for x in x_array:
        I = integrals.integrate_with_simpsons_rule(function, 0, x, 100)
        y_array.append(I)
    plt.plot(x_array, y_array)
    plt.xlabel('x')
    plt.ylabel('E(x)')
    plt.show()


if __name__ == "__main__":
    main()

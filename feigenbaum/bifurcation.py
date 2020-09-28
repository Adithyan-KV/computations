import matplotlib.pyplot as plt
import numpy as np


def main():
    plot_feigenbaum()


def plot_feigenbaum():
    r_values = np.arange(1, 4, 0.001)
    x_values = np.zeros(r_values.size, float)+0.5

    for _ in range(1001):
        x_values = logistic(r_values, x_values)

    for _ in range(4):
        for _ in range(1005):
            x_values = logistic(r_values, x_values)
        plt.plot(r_values, x_values, 'k.', alpha=0.5)
    plt.xlabel('r')
    plt.ylabel('x')
    plt.title('Feigenbaum Plot')
    plt.show()


def logistic(r, x):
    return r*x*(1.0-x)


def plot_logistic(r):
    x_array = np.linspace(0, 1, 100)
    y_array = np.zeros(100)
    for i in range(x_array.shape[0]):
        y = logistic(r, x_array[i])
        y_array[i] = y
    plt.plot(x_array, y_array)
    plt.xlabel("x")
    plt.ylabel("rx(1-x)")
    plt.legend([f'r = {r}'])
    plt.show()


if __name__ == "__main__":
    main()

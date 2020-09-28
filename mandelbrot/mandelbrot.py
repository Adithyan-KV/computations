import cmath
import numpy as np
import matplotlib.pyplot as plt


def main():
    grid_size = 100
    points_grid = np.zeros((grid_size, grid_size))
    min_value = -2
    max_value = 2
    x_points = np.arange(min_value, max_value, (max_value-min_value)/grid_size)
    y_points = np.arange(min_value, max_value, (max_value-min_value)/grid_size)
    for i, x in enumerate(x_points):
        for j, y in enumerate(y_points):
            z = complex(0, 0)
            c = complex(x, y)
            for _ in range(100):
                z = iteration(z, c)
                if abs(z) > 2:
                    points_grid[j, i] = 1
                    break
    plt.matshow(points_grid)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title('Mandelbrot set')
    plt.show()


def iteration(z, c):
    return z**2+c


if __name__ == "__main__":
    main()

import cmath
import math
import numpy as np
import matplotlib.pyplot as plt


def main():
    grid_size = 500
    points_grid = np.zeros((grid_size, grid_size))
    x_min = -2
    x_max = 1
    y_min = -1.5
    y_max = 1.5
    x_points = np.arange(x_min, x_max, (x_max-x_min)/grid_size)
    y_points = np.arange(y_min, y_max, (y_max-y_min)/grid_size)
    for i, x in enumerate(x_points):
        for j, y in enumerate(y_points):
            z = complex(0, 0)
            c = complex(x, y)
            for k in range(100):
                z = iteration(z, c)
                if abs(z) > 2:
                    points_grid[j, i] = 1-(math.log(k + 1, 10)/10)
                    break
    plt.imshow(points_grid)
    plt.colorbar()
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.axis('off')
    plt.title(f'Mandelbrot set({grid_size}x{grid_size})')
    plt.savefig('mandelbrot_log.jpg', dpi=320)
    plt.show()


def iteration(z, c):
    return z**2+c


if __name__ == "__main__":
    main()

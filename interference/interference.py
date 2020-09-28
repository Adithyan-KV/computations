import math
import matplotlib.pyplot as plt
import numpy as np


def main():
    grid_size = 100
    points_grid = np.zeros((grid_size, grid_size))
    # all units in cms
    amplitude1 = 1
    wavelength1 = 5
    k1 = (2*math.pi)/wavelength1
    amplitude2 = 1
    wavelength2 = 2.5
    k2 = (2*math.pi)/wavelength2

    # position of two sources in the coordinate system
    seperation = 40
    total_side_length = 100
    x1 = total_side_length/2 + seperation/2
    y1 = total_side_length/2
    x2 = total_side_length/2 - seperation/2
    y2 = total_side_length/2

    # calculating interference
    for i in range(grid_size):
        for j in range(grid_size):
            r1 = math.sqrt((i-x1)**2+(j-y1)**2)
            r2 = math.sqrt((i-x2)**2+(j-y2)**2)
            resultant_amplitude = amplitude1 * \
                math.sin(k1*r1)+amplitude2*math.sin(k2*r2)
            points_grid[j][i] = resultant_amplitude

    plt.matshow(points_grid)
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    main()

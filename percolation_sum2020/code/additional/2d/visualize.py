import matplotlib.pyplot as plt
import numpy as np

COLOR_WHITE = 0
COLOR_BLACK = 1

EMPTY = COLOR_WHITE
BUSY = COLOR_BLACK


def draw_array_as_grid(figure, grid):
    plt.figure(figure)
    plt.imshow(grid, cmap='binary', vmin=np.min(grid), vmax=np.max(grid))


def map_dict_on_grid(grid, dictionary):
    for key in list(dictionary.keys()):
        for val in dictionary[key]:
            grid[val[0]][val[1]] = key

    return grid

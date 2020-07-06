import time

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


with open("/Users/me/Documents/cw4/code/percolation/python/modeling3d/direct/log/direct_creation_time_arr.txt", "r") as f:
    arr = np.loadtxt(f)

    x_arr = range(len(arr))

    p = np.polyfit(x_arr, arr, 3)
    y = np.polyval(p, x_arr)

    plt.plot(x_arr, arr, label='original', linewidth=0.5)
    plt.plot(x_arr, y, label='mnk', linewidth=3)
    plt.legend()
    plt.show()
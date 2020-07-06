import random

import numpy as np


def generate_3d_cluster(size: int, probability):
    final_cube = np.zeros((size, size, size), bool)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                final_cube[i][j][k] = True if random.random() <= probability else False

    return final_cube

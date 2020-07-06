import numpy as np 
from matplotlib import pyplot as plt
from random import randint
from math import sin

size = 300

res_arr = np.zeros((size, size), int)

black = 0
white = 1000


fig, ax = plt.subplots()


for i in range(size):
    for j in range(size):
        res_arr[i][j] = white #randint((white + black) * (1/4), (white + black) * (3 / 4))

ax.imshow(res_arr, cmap='gray', vmin=black, vmax=white)

for i in range(1, 25):
    x = i * (int(size / 25))
    for j in range(0, 25):
        if (randint(1, 3) < 3):
            y = j * (int(size / 25))
            l = plt.Line2D([x, x], [y + 3, y + (int(size / 25)) - 3], linewidth=1, color='gray')
            ax.add_artist(l)

    y = i * (int(size / 25))
    for j in range(0, 25):
        if (randint(1, 3) < 3):
            x = j * (int(size / 25))
            l = plt.Line2D([x + 3, x + (int(size / 25)) - 3], [y, y], linewidth=1, color='gray', zorder=1)
            ax.add_artist(l)

for i in range(100):
    x = randint(0, 24) * (int(size / 25))
    y = randint(0, 24) * (int(size / 25))

    c = plt.Circle((x, y), radius=3, color='black', zorder=4)

    ax.add_patch(c)
# for i in range(randint(40, 570)):
#     x_val = randint(0, 24) * (int(size / 25))
#     y_start = randint(0, 24) * (int(size / 25))
#     y_end = randint(0, 24) * (int(size / 25))

#     for j in range(y_start, y_start + (int(size / 25))):
#         for k in range(x_val, x_val + 1):
#             res_arr[j][k] = white
            

#     y_val = randint(0, 24) * (int(size / 25))
#     x_start = randint(0, 24) * (int(size / 25))

#     for j in range(x_start, x_start + (int(size / 25))):
#         for k in range(y_val, y_val + 1):
#             res_arr[k][j] = white


plt.show()
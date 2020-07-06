import numpy as np 
from matplotlib import pyplot as plt
from random import randint
from math import sin

size = 100

res_arr = np.zeros((size, size), int)

black = 1000
white = 0

for i in range(size):
    for j in range(size):
        res_arr[i][j] = black #randint((white + black) * (1/4), (white + black) * (3 / 4))


for i in range(randint(40, 570)):
    x_val = randint(0, 24) * (int(size / 25))
    y_start = randint(0, 24) * (int(size / 25))
    y_end = randint(0, 24) * (int(size / 25))

    for j in range(y_start, y_start + (int(size / 25))):
        for k in range(x_val, x_val + 1):
            res_arr[j][k] = white
            

    y_val = randint(0, 24) * (int(size / 25))
    x_start = randint(0, 24) * (int(size / 25))

    for j in range(x_start, x_start + (int(size / 25))):
        for k in range(y_val, y_val + 1):
            res_arr[k][j] = white

plt.imshow(res_arr, 'gray')

plt.show()
import time
from matplotlib import pyplot as plt 
from numpy import core as np, savetxt, loadtxt
from calculation import get_grid, NOT_CHECKED, EMPTY
from visualize import draw_array_as_grid

probability = 0.3

grid_size = 100

grid_creation_speed_direct = []
init_grid = get_grid(grid_size, probability, variant1=1, variant2=0)

draw_array_as_grid("2d_cluster_example", init_grid)
plt.show()


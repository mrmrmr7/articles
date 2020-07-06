from visualize import impose_cube_on_figure

import time
from numpy import core as np, savetxt, loadtxt
from calculation import generate_3d_cluster

grid_size = 100
probability = 0.2


probability = 0.3

grid_size_arr = np.array(range(100))
repeat_n = 10

grid_creation_speed_direct = []

for grid_size in grid_size_arr:
    print(f"calculate from {len(grid_size_arr)} for {grid_size}")
    
    res_t = 0
    for i in range(repeat_n):
        start = time.time()
        init_grid = generate_3d_cluster(grid_size, probability)
        end = time.time()
        res_t += (end - start)

    grid_creation_speed_direct.append(res_t/repeat_n)

with open("/Users/me/Documents/cw4/code/percolation/python/modeling3d/direct/log/direct_creation_time_arr.txt", "w+") as f:
    savetxt(f, np.array(grid_creation_speed_direct).reshape((1, len(grid_creation_speed_direct))))

import time
from numpy import core as np, savetxt, loadtxt
from ..calculation import get_grid, NOT_CHECKED, EMPTY

probability = 0.5

grid_size_arr = np.array(range(1000))
repeat_n = 20

grid_creation_speed_direct = []

for grid_size in grid_size_arr:
    print(f"calculate from {len(grid_size_arr)} for {grid_size}")
    
    res_t = 0
    for i in range(repeat_n):
        start = time.time()
        init_grid = get_grid(grid_size, probability, variant1=NOT_CHECKED, variant2=EMPTY)
        end = time.time()
        res_t += (end - start)

    grid_creation_speed_direct.append(res_t/repeat_n)

with open("/Users/me/Documents/cw4/code/additional/2d/cluster_creation_speed_test/log/direct_creation_time_arr.txt", "w+") as f:
    savetxt(f, np.array(grid_creation_speed_direct).reshape((1, len(grid_creation_speed_direct))))

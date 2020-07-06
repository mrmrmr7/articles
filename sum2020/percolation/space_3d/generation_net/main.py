from matplotlib import pyplot as plt
from visualize import impose_cube_on_figure

from calculation import generate_3d_cluster


grid_size = 10
probability = 0.2

cubeGrid = generate_3d_cluster(grid_size, probability)

impose_cube_on_figure('Corn cluster', cubeGrid)

plt.show()

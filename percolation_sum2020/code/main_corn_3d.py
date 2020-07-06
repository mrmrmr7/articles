from matplotlib import pyplot as plt
from space_3d.generation_corn.visualize import impose_cube_on_figure

from space_3d.generation_corn.calculation import generate_3d_cluster


grid_size = 10
probability = 0.29

cubeGrid = generate_3d_cluster(grid_size, probability)

impose_cube_on_figure('Corn cluster', cubeGrid)

plt.show()

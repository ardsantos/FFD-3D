import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")


def x_y_edge(x_range, y_range, z_range):        #comented lines in axes3d.py: 1636 and 1849
    xx, yy = np.meshgrid(x_range, y_range)

    for value in [0, 1]:
        ax.plot_wireframe(xx, yy, z_range[value], color="r")
        ax.plot_surface(xx, yy, z_range[value], color="r", alpha=0.2)


def y_z_edge(x_range, y_range, z_range):
    yy, zz = np.meshgrid(y_range, z_range)

    for value in [0, 1]:
        ax.plot_wireframe(x_range[value], yy, zz, color="r")
        ax.plot_surface(x_range[value], yy, zz, color="r", alpha=0.2)


def x_z_edge(x_range, y_range, z_range):
    xx, zz = np.meshgrid(x_range, z_range)

    for value in [0, 1]:
        ax.plot_wireframe(xx, y_range[value], zz, color="r")
        ax.plot_surface(xx, y_range[value], zz, color="r", alpha=0.2)


def rect_prism(x_range, y_range, z_range):
    x_y_edge(x_range, y_range, z_range)
    y_z_edge(x_range, y_range, z_range)
    x_z_edge(x_range, y_range, z_range)


def main():
    rect_prism(np.array([-1, 1]),
               np.array([-1, 1]),
               np.array([-0.5, 0.5]))
    rect_prism(np.array([1,2]),
               np.array([1,2]),
               np.array([0.5,1.5]))           
    plt.show()

if __name__ == '__main__':
    main()

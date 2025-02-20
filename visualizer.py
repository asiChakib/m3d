import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from asg1 import *

o = (0,0,0)
vert, edg = regular_prism(o, 2, 2, 6)



def scatter_prism(vert):
    ver = np.array(vert)
    x, y, z = ver[:, 0], ver[:, 1], ver[:, 2]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c='b', marker='o')  # 'c' for color, 'o' for marker style

    ax.plot([0, max(x)], [0, 0], [0, 0], color='r', linewidth=2, label="X-axis")  # X-axis in red
    ax.plot([0, 0], [0, max(y)], [0, 0], color='g', linewidth=2, label="Y-axis")  # Y-axis in green
    ax.plot([0, 0], [0, 0], [0, max(z)], color='b', linewidth=2, label="Z-axis")  # Z-axis in blue

    # Labels
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("3D Scatter Plot")

    plt.show()
    
#scatter_prism(vert)

print(len(edg))

def plot_lines(line_segments):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for start, end in line_segments:
        x_coords = [start[0], end[0]]
        y_coords = [start[1], end[1]]
        z_coords = [start[2], end[2]]

        ax.plot(x_coords, y_coords, z_coords, marker='o')

    # Set labels and equal aspect ratio
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio for 3D

    plt.show()

plot_lines(edg)
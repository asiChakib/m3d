import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def regular_prism(origin, height, radius, faces):
    # assume that faces >= 3
    vertices, edges = [], []
    ox, oy, oz = origin
    vertices.append((ox + radius, oy, oz))
    alpha = 2 * np.pi / faces
    for i in range(1, faces):
        vertices.append((ox + radius * np.cos(alpha * i), 
                         oy + radius * np.sin(alpha * i),
                         oz))
        
    
    vertices2 = []
    for item in vertices:
        
        #========================
        it = list(item)
        it[-1] += height
        vertices2.append(tuple(it))
        
    vertices.extend(vertices2)
    del vertices2
        
    return edges

o = (0,0,0)
vert = regular_prism(o, 3, 1, 4)



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

print(vert)
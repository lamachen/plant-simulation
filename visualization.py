
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from growth_algorithm import Plant

def visualize_plant(plant):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x, y, z = [], [], []
    for i, cell in enumerate(plant.cells):
        x.append(i)
        y.append(i)
        z.append(i)
    
    ax.scatter(x, y, z, c='green', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    
    plt.show()

if __name__ == '__main__':
    plant = Plant()
    plant.simulate_growth(10)
    visualize_plant(plant)


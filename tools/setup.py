import matplotlib.pyplot as plt
import numpy as np



def plot_vector(v, origin=[0, 0], color='r', label=None):
    """ 
    Plot a vector on a 2D plane.
    """
    plt.quiver(*origin, *v, angles='xy', scale_units='xy', scale=1, color=color, label=label)
    

def plot_paper_with_vector(vectors, colors, labels, xlim=(-5, 5), ylim=(-5, 5), title="Vector Plot"):
    """ 
    Set up a 2D grid and plot multiple vectors.
    
    """
    plt.figure(figsize=(5, 5))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xticks(range(int(xlim[0]), int(xlim[1]) + 1, 1))
    plt.yticks(range(int(ylim[0]), int(ylim[1]) + 1, 1))
    
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    for v, color, label in zip(vectors, colors, labels):
        plot_vector(v, color=color, label=label)
    
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(title)
    plt.show()
    
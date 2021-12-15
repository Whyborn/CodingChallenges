from get_input import get_data, split_on_lines
import numpy as np
import sys

year, day = 2021, 15

class Node:

    def __init__(self, path_length):
        self.path_length = sys.maxsize
        self.visited = False

    def take_smallest_distance(self, new_length):
        self.path_length = min(new_length, path_length)


data = np.array([[int(var) for var in line] for line in split_on_lines(get_data(year, day))])

data = np.array([[1, 8, 1, 1, 1], [1, 1, 1, 8, 1], [4, 2, 8, 8, 1], [1, 5, 8, 8, 1]])

# What we want to do is map the grid out in terms of path
# Start from the bottom and work up
def minimum_path(grid, i, j):
    n, m = np.shape(grid)
    # Reached past grid edge
    if (i < 0 or j < 0):
        return sys.maxsize
    # Reached the start- don't add it
    elif (i == 0 and j == 0):
        return grid[i, j]
    else:
        return grid[i, j] + new_min(minimum_path(grid, i-1, j), minimum_path(grid, i, j-1))

def new_min(x, y):
    return x if (x < y) else y
n, m = np.shape(data)
i, j = n-1, m-1

print(minimum_path(data, i, j))

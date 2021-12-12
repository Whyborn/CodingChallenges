from get_input import get_data, split_on_lines
import numpy as np

data = split_on_lines(get_data(2021, 5))

paths = [[[int(val) for val in pair.split(',')] for pair in path.split(' -> ')] for path in data]

grid = np.zeros((1000, 1000))

for path in paths:
    start_point, end_point = path
    if (start_point[0] == end_point[0]):
        #print(f"A straight path from {start_point} to {end_point}")
        grid[start_point[0], min(start_point[1], end_point[1]):max(start_point[1], end_point[1]) + 1] += 1
    elif (start_point[1] == end_point[1]):
        #print(f"A straight path from {start_point} to {end_point}")
        grid[min(start_point[0], end_point[0]):max(start_point[0], end_point[0]) + 1, start_point[1]] += 1
    elif (abs(start_point[0] - end_point[0]) == abs(start_point[1] - end_point[1])):
        # For the sake of cleanliness, define the range objects prior
        if start_point[0] < end_point[0]:
            i_range = range(start_point[0], end_point[0] + 1)
            j_range = range(start_point[1], end_point[1] + 1) if end_point[1] > start_point[1] else range(start_point[1], end_point[1] - 1, -1)
        else:
            i_range = range(end_point[0], start_point[0] + 1)
            j_range = range(end_point[1], start_point[1] + 1) if end_point[1] < start_point[1] else range(end_point[1], start_point[1] - 1, -1)
        for i, j in zip(i_range, j_range):
            grid[i, j] += 1

    else:
        print(f"A path that doesn't fit our definition? {start_point}, {end_point}")

# for i in range(1000):
    # for j in range(1000):
        # if grid[i, j] > 1:
            # print(f"Coordinate ({i}, {j}) has {grid[i,j]} intersecting paths")

print(np.sum(np.ones_like(grid)[grid >= 2]))

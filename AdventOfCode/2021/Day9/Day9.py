from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 9 

data = split_on_lines(get_data(year, day))
# data = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".split("\n")

data = np.array([[int(var) for var in string] for string in data])

n, m = np.shape(data)

risk_level = 0

low_points = []


for i in range(n):
    for j in range(m):
        neighbours = []
        try:
            neighbours.append(data[i+1, j])
        except:
            pass
        try:
            neighbours.append(data[i-1, j])
        except:
            pass
        try:
            neighbours.append(data[i, j+1])
        except:
            pass
        try:
            neighbours.append(data[i, j-1])
        except:
            pass

        if np.all(data[i, j] < neighbours):
            risk_level += data[i, j] + 1
            low_points.append((i, j))

# Part 2

basin_map = (data == 9).astype(int)

def spread_out(floor_map, curr_point, explored):

    # Take the current point and check its neighbours
    neighbours = []
    i, j = curr_point
    if (i + 1) < n:
        neighbour = floor_map[i+1, j]
        if not neighbour and ((i+1, j) not in explored):
            neighbours.append((i+1, j))
            explored.append((i+1, j))

    if (i - 1) >= 0:
        neighbour = floor_map[i-1, j]
        if not neighbour and ((i-1, j) not in explored):
            neighbours.append((i-1, j))
            explored.append((i-1, j))

    if (j + 1) < m:
        neighbour = floor_map[i, j+1]
        if not neighbour and ((i, j+1) not in explored):
            neighbours.append((i, j+1))
            explored.append((i, j+1))

    if (j - 1) >= 0:
        neighbour = floor_map[i, j-1]
        if not neighbour and ((i, j-1) not in explored):
            neighbours.append((i, j-1))
            explored.append((i, j-1))

    if len(neighbours) == 0:
        return
    else:
        for point in neighbours:
            spread_out(floor_map, point, explored)

basin_size = []

for start_point in low_points:
    points_in_basin = [start_point]

    spread_out(basin_map, start_point, points_in_basin)

    basin_size.append(len(points_in_basin))

total = 1

for _ in range(3):
    total *= basin_size.pop(basin_size.index(max(basin_size)))

print(total)

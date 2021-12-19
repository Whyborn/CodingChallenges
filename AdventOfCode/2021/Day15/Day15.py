from get_input import get_data, split_on_lines
import numpy as np
import sys
import copy
import heapq as heap

year, day = 2021, 15

class Node:

    def __init__(self, index):
        self.path_length = sys.maxsize
        self.visited = False
        self.index = index

    def take_smallest_distance(self, new_length):
        self.path_length = min(new_length, self.path_length)

    def is_visited(self):
        self.visited = True

    def __repr__(self):
        if self.visited:
            return f"Node at {self.index} has path length {self.path_length} is visited"
        else:
            return f"Node at {self.index} has path length {self.path_length} is not visited"

    def __lt__(self, other):
        return self.path_length < other.path_length

    # def __eq__(self, other)
        # return self.path_length == other.path_length

    def __gr__(self, other):
        return self.path_length > other.path_length


def key_for_min(node):
    if node.visited:
        return sys.maxsize
    else:
        return node.path_length

def find_path(cost_grid):
    # Create the cost grid and the grid of nodes
    node_grid = [[Node((i, j)) for j, _ in enumerate(line)] for i, line in enumerate(cost_grid)]
    n, m = len(cost_grid), len(cost_grid[0])

    # Set the starting node length to 0
    node_grid[0][0].take_smallest_distance(0)
    node_grid[0][0].is_visited()
    i, j = 0, 0

    unvisited_nodes = []
    while not (i == (n-1) and j == (m-1)):
        for i_shift in [-1, 1]:
            if ((i + i_shift) >= 0 and (i + i_shift) < n) and not node_grid[i + i_shift][j].visited:
                node_grid[i + i_shift][j].take_smallest_distance(node_grid[i][j].path_length + cost_grid[i + i_shift][j])
                if node_grid[i + i_shift][j] not in unvisited_nodes:
                    unvisited_nodes.append(node_grid[i + i_shift][j])

        for j_shift in [-1, 1]:
            if ((j + j_shift) >= 0 and (j + j_shift) < m) and not node_grid[i][j + j_shift].visited:
                node_grid[i][j + j_shift].take_smallest_distance(node_grid[i][j].path_length + cost_grid[i][j + j_shift])
                if node_grid[i][j + j_shift] not in unvisited_nodes:
                    unvisited_nodes.append(node_grid[i][j + j_shift])

        next_node = min(unvisited_nodes, key = key_for_min)
        unvisited_nodes.pop(unvisited_nodes.index(next_node))
        
        next_node.is_visited()
        i, j = next_node.index

        print(i, j)
    return node_grid[i][j].path_length

def find_path_heapq(cost_grid):
    # Create the cost grid and the grid of nodes
    node_grid = [[Node((i, j)) for j, _ in enumerate(line)] for i, line in enumerate(cost_grid)]
    n, m = len(cost_grid), len(cost_grid[0])

    # Set the starting node length to 0
    node_grid[0][0].take_smallest_distance(0)
    node_grid[0][0].is_visited()
    i, j = 0, 0

    unvisited_nodes = []
    while not (i == (n-1) and j == (m-1)):
        for i_shift in [-1, 1]:
            if ((i + i_shift) >= 0 and (i + i_shift) < n) and not node_grid[i + i_shift][j].visited:
                node_grid[i + i_shift][j].take_smallest_distance(node_grid[i][j].path_length + cost_grid[i + i_shift][j])
                if node_grid[i + i_shift][j] not in unvisited_nodes:
                    heap.heappush(unvisited_nodes, node_grid[i + i_shift][j])
        for j_shift in [-1, 1]:
            if ((j + j_shift) >= 0 and (j + j_shift) < m) and not node_grid[i][j + j_shift].visited:
                node_grid[i][j + j_shift].take_smallest_distance(node_grid[i][j].path_length + cost_grid[i][j + j_shift])
                if node_grid[i][j + j_shift] not in unvisited_nodes:
                    heap.heappush(unvisited_nodes, node_grid[i][j + j_shift])

        
        next_node = heap.heappop(unvisited_nodes)

        next_node.is_visited()
        i, j = next_node.index

        print(i, j)
    return node_grid[i][j].path_length

cost_grid = [[int(var) for var in line] for line in split_on_lines(get_data(year, day))]

#print(f"For the single grid, minimum cost path is: {find_path(cost_grid)})")

#Part 2
orig_grid = copy.deepcopy(cost_grid)

for col_count in range(1, 5):
    for row_id, row in enumerate(orig_grid):
        cost_grid[row_id] += [(num + col_count) % 10 + 1 if (num + col_count) >= 10 else num + col_count for num in row]

orig_grid = copy.deepcopy(cost_grid)

for row_count in range(1, 5):
    cost_grid += [[(num + row_count) % 10 + 1 if (num + row_count) >= 10 else num + row_count for num in row] for row in orig_grid]

print(f"For the 5x5 grid, minimum cost path is: {find_path(cost_grid)})")

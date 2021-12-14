from get_input import get_data, split_on_lines
import numpy as np
import string

lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)

year, day = 2021, 12 

data = split_on_lines(get_data(year, day))

class Cave:

    def __init__(self, name):

        self.name = name
        self.connected_caves = []

    def add_connection(self, other):

        self.connected_caves.append(other)

class Small_Cave(Cave):

    def __init__(self, name):
        super().__init__(name)

class Large_Cave(Cave):

    def __init__(self, name):
        super().__init__(name)

def proceed_forward(start, current_path, small_caves, large_caves, total_paths):

    # Treat 'start' as the current point for any path
    if start in small_caves.keys():
        start_cave = small_caves[start]
    elif start in large_caves.keys():
        start_cave = large_caves[start]
    elif start == "end":
        total_paths.append(current_path + ["end"])
        return
    else:
        raise ValueError(f"The start point is {start}, the path is {current_path}, how did we get here?")

    # Where can we go?
    for next_cave in start_cave.connected_caves:
        # print(next_cave, current_path)
        # For Part 1, use this line for the small cave logic
        # if (next_cave in small_caves.keys()) and (next_cave not in current_path):

        # For Part 2, use this line for the small cave logic
        if (next_cave in small_caves.keys()) and (is_path_valid(current_path, next_cave, small_caves)):
            #print("Its a small cave that isn't in the current path")
            new_path = current_path + [next_cave]
            print(new_path)
            proceed_forward(next_cave, new_path, small_caves, large_caves, total_paths)

        elif (next_cave in large_caves.keys()):
            new_path = current_path + [next_cave]
            proceed_forward(next_cave, new_path, small_caves, large_caves, total_paths)

        elif (next_cave == "end"):
            total_paths.append(current_path + ["end"])

#------- Finish proceed forward ---------#

def is_path_valid(current_path, next_cave, small_caves):

    # Count the occurrences of each small cave
    cave_counter = {}
    for small_cave in small_caves.keys():
        cave_counter[small_cave] = (current_path + [next_cave]).count(small_cave)

    return not (list(cave_counter.values()).count(2) > 1 or max(list(cave_counter.values())) > 2)

#------- Finish is_path_valid -------#


def Part1(data):
    # First, let's build a list of the caves
    start_connections = []
    small_caves = {}
    large_caves = {}
    for path in data:
        cave_pair = path.split("-")
        for num, cave in enumerate(cave_pair):

            # Keep track of which caves connect to the start
            if cave == "start":
                start_connections.append(cave_pair[num-1])

            # Don't care if the current cave is an end, just that the correct other caves connect to it
            elif cave == "end":
                pass

            # We know the cave IDs must either be all upper or all lower case, so can just check against first element
            elif cave[0] in lower_case:
                if cave not in small_caves.keys():
                    small_caves[cave] = Small_Cave(cave)

                if cave_pair[num-1] != "start" and (cave_pair[num-1] not in small_caves[cave].connected_caves):
                    small_caves[cave].add_connection(cave_pair[num-1])
                
            elif cave[0] in upper_case:
                if cave not in large_caves.keys():
                    large_caves[cave] = Large_Cave(cave)

                if cave_pair[num-1] != "start" and (cave_pair[num-1] not in large_caves[cave].connected_caves):
                    large_caves[cave].add_connection(cave_pair[num-1])

    # Now we should have a list of all the connections
    for cave in small_caves.keys():
        print(f"Small cave {cave} has connections {small_caves[cave].connected_caves}")
    for cave in large_caves.keys():
        print(f"Large cave {cave} has connections {large_caves[cave].connected_caves}")

    total_paths = []
    for start_point in start_connections:
        current_path = ["start", start_point]
        # if start_point in large_caves.keys():
            # print(f"Path {start_point} has connections {large_caves[start_point].connected_caves}")
        # elif start_point in small_caves.keys():
            # print(f"Path {start_point} has connections {small_caves[start_point].connected_caves}")
        proceed_forward(start_point, current_path, small_caves, large_caves, total_paths)

    print(len(total_paths))

# Do Part 1
Part1(data)

# Part 2 is the same, with one line changed









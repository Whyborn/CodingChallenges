from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 11 

data = np.array([[int(val) for val in line] for line in split_on_lines(get_data(year, day))])

num_flashes = 0
n, m = np.shape(data)

# Part 1
# for _ in range(100):
    
    # # The first stage- all numbers increase by 1
    # data = data + 1

    # # Things to track whether we're finished a step
    # completed_step = False
    # flashed = []

    # while not completed_step:
        # completed_step = True
        # about_to_flash = []
        # # Which ones are currently at max energy?
        # for i in range(n):
            # for j in range(m):
                # if data[i, j] == 10 and ((i, j) not in flashed):
                    # completed_step = False
                    # about_to_flash.append((i, j))

        # # Which ones are getting energy from a nearby thing?
        # for index in about_to_flash:
            # for y in range(max(0, index[0]-1), min(n, index[0]+2)):
                # for z in range(max(0, index[1]-1), min(m, index[1]+2)):
                    # if (y, z) != index:
                        # data[y, z] = data[y, z] if data[y, z] == 10 else data[y, z] + 1

        # flashed += about_to_flash 
    # # Step is completed, count the flashes and resets the 9s to 0s
    # num_flashes += len(data[data == 10])

    # data[data == 10] = 0

#print(num_flashes)

# Part 2 

for a in range(1000):
    
    # The first stage- all numbers increase by 1
    data = data + 1

    # Things to track whether we're finished a step
    completed_step = False
    flashed = []

    while not completed_step:
        completed_step = True
        about_to_flash = []
        # Which ones are currently at max energy?
        for i in range(n):
            for j in range(m):
                if data[i, j] == 10 and ((i, j) not in flashed):
                    completed_step = False
                    about_to_flash.append((i, j))

        # Which ones are getting energy from a nearby thing?
        for index in about_to_flash:
            for y in range(max(0, index[0]-1), min(n, index[0]+2)):
                for z in range(max(0, index[1]-1), min(m, index[1]+2)):
                    if (y, z) != index:
                        data[y, z] = data[y, z] if data[y, z] == 10 else data[y, z] + 1

        flashed += about_to_flash 
    # Step is completed, count the flashes and resets the 9s to 0s
    num_flashes += len(data[data == 10])

    if np.all(data == 10): break

    data[data == 10] = 0

print(a+1)

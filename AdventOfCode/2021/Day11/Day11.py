from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 11 

data = np.array([[int(val) for val in line] for line in split_on_lines(get_data(year, day))])

num_flashes = 0
n, m = np.shape(data)

for _ in range(2):
    
    # The first stage- all numbers increase by 1
    data = data + 1

    while np.any(data) == 9:
        about_to_flash = []
        for i in range(n):
            for j in range(m):
                if data[i, j] == 9:
                    about_to_flash.append((i, j))

        for index in about_to_flash:
            for y in range(max(0, index[0]-1), min(n-1, index[0]+2)):
                for z in range(max(0, index[1]-1), min(m-1, index[1]+2)):
                    if (y, z) != index:
                        data[y, z] = data[y, z] if data[y, z] == 9 else data[y, z] + 1





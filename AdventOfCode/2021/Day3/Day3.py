from get_input import get_data, split_on_lines 
import numpy as np

data = split_on_lines(get_data(2021, 3))

length = len(data[0])
zero_count = [0] * length
one_count = [0] * length
for bit in data:
    for j in range(length):
        if bit[j] == "0":
            zero_count[j] += 1
        elif bit[j] == "1":
            one_count[j] += 1
main_str = ["0" if zero_count[j] > one_count[j] else "1" for j in range(length)]
other_str = ["1" if zero_count[j] > one_count[j] else "0" for j in range(length)]
main = int("".join(main_str), 2)
other = int("".join(other_str), 2)

# Part 2

#Convert to numpy arrays

data_as_array = np.array([[int(val) for val in reading] for reading in data])
n, m = np.shape(data_as_array)
for col in range(m):

    flag_for_removal = []
    most_common = 1 if np.sum(data_as_array[:, col]) / n >= 0.5 else 0
    
    for row in range(n):

        if data_as_array[row, col] != most_common:
            flag_for_removal.append(row)

    for flag in flag_for_removal[::-1]:
        if np.shape(data_as_array)[0] == 1:
            break
        data_as_array = np.delete(data_as_array, flag, 0)

    n, m = np.shape(data_as_array)

O2_reading = int("".join(str(val) for val in data_as_array[0]), 2)

data_as_array = np.array([[int(val) for val in reading] for reading in data])
n, m = np.shape(data_as_array)
for col in range(m):

    flag_for_removal = []
    most_common = 0 if np.sum(data_as_array[:, col]) / n >= 0.5 else 1
    
    for row in range(n):

        if data_as_array[row, col] != most_common:
            flag_for_removal.append(row)

    for flag in flag_for_removal[::-1]:
        if np.shape(data_as_array)[0] == 1:
            break
        data_as_array = np.delete(data_as_array, flag, 0)

    n, m = np.shape(data_as_array)

CO2_reading = int("".join(str(val) for val in data_as_array[0]), 2)

print(O2_reading * CO2_reading)



    
 

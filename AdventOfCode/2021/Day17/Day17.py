from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 17

data = get_data(year, day)

x_part, y_part = data.split(',')
_, x_range = x_part.split("=")
_, y_range = y_part.split("=")

x_target, y_target = [int(num) for num in x_range.split("..")], [int(num) for num in y_range.split("..")]

# The positions are just sums of arithmetic series
# We know the maximum limits of both x and y
# The initial x velocity cannot be greater than the max x range,
# The magnitude of the initial y velocity cannot be greater than the min y range

def calc_y_series_sum(init, step, diff):
    return int(step / 2. * (2 * init + (step - 1) * diff))

def calc_x_series_sum(init, step, diff):
    if step <= init:
        return int(step / 2. * (2 * init + (step - 1) * diff))
    else:
        return int(init / 2. * (2 * init + (init - 1) * diff))

xvel_range = range(0, x_target[1]+1); yvel_range = range(y_target[0], -y_target[0])

print(calc_x_series_sum(5, 20, -1))

#Run through the valid y velocities
possible_velocities = []
count = 0
for yvel in yvel_range:
    print(f"Starting y velocity of {yvel}")
    step = 1; y_pos = 0
    while 1:
        # Current position
        y_pos = calc_y_series_sum(yvel, step, -1)

        # If it falls in the desired box, check x locations
        if y_pos >= y_target[0] and y_pos <= y_target[1]:
            for xvel in xvel_range:
                print(f"Starting x velocity of {xvel}")
                x_pos = calc_x_series_sum(xvel, step, -1)
                if x_pos >= x_target[0] and x_pos <= x_target[1] and ((xvel, yvel) not in possible_velocities):
                    count += 1
                    possible_velocities.append((xvel, yvel))
        elif y_pos < y_target[0]:
            break

        step += 1

print(count)


    


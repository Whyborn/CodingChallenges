from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 17

data = get_data(year, day)

x_part, y_part = data.split(',')
_, x_range = x_part.split("=")
_, y_range = y_part.split("=")

x_target, y_target = x_range.split(".."), y_range.split("..")

def calc_trajectory(initial_vel, x_target, y_target):
    pos = [0, 0]
    vel = initial_vel

    while 1:
        pos[0] += vel[0]
        pos[1] += vel[1]

        if (pos[0] > x_target[0]) and (pos[0] < x_target[1]) and (pos[1] > y_target[0]) and (pos[1] < y_target[1]):
            break


        vel[0] -= 1 * np.sign(vel[0])
        vel[1] -= 1


    


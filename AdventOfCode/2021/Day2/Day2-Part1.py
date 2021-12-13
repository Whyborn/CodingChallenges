import sys
sys.path.append('../..')
from get_input import get_data, split_on_lines

data = split_on_lines(get_data(2021, 2))

hor_pos, ver_pos = 0, 0
for command in data:
    direction, dist = command.split()
    if direction == "forward":
        hor_pos += int(dist)
    elif direction == "down":
        ver_pos += int(dist)
    elif direction == "up":
        ver_pos -= int(dist)

print(ver_pos * hor_pos)

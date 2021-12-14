import sys
sys.path.append('../../')
from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 13 

data = split_on_lines(get_data(year, day))
# data = split_on_lines("""6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5""")


split_point = data.index('')
dots = [tuple([int(var) for var in line.split(',')[::-1]]) for line in data[:split_point]]
folds = data[split_point+1:]

# Maybe base it on the fold locations?
found_x_size = False
found_y_size = False
for fold in folds:
    cmd_point = fold.index("=")
    direction = fold[cmd_point-1]
    fold_line = int(fold[cmd_point+1:])

    if direction == "x" and not found_x_size:
        found_x_size = True
        j_size = 2 * fold_line + 1

    elif direction == "y" and not found_y_size:
        found_y_size = True
        i_size = 2 * fold_line + 1

    if found_x_size and found_y_size:
        break

paper = np.zeros((i_size, j_size), dtype = int)

for index in dots:
    paper[index] = 1

print(len(paper[paper == 1]))

for num, fold in enumerate(folds):
    # Find location of the '='
    cmd_point = fold.index("=")
    direction = fold[cmd_point-1]
    fold_line = int(fold[cmd_point+1:])

    m, n = np.shape(paper)

    if direction == "x":
        print(f"Folding along the vertical line x={fold_line}, with paper size {(m, n)}")

        paper = np.logical_or(paper[:, :fold_line], np.flip(paper[:, fold_line+1:], axis = 1))

    elif direction == "y":
        print(f"Folding along the horizontal line y={fold_line}, with paper size {(m, n)}")

        paper = np.logical_or(paper[:fold_line, :], np.flip(paper[fold_line+1:, :], axis = 0))

    print(len(paper[paper == 1]))

import matplotlib.pyplot as mpl

mpl.figure()
mpl.imshow(paper.astype('uint8'), interpolation = 'nearest')
mpl.savefig("output.png")
mpl.close()

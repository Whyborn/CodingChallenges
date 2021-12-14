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

# Assume the size of the paper is the maximum of the x and y coordinates
i_size, j_size = zip(*dots)
i_size, j_size = max(i_size) + 1, max(j_size) + 1

paper = np.zeros((i_size, j_size), dtype = int)

for index in dots:
    paper[index] = 1

print(paper[39, 8])
print(paper[39, :100])

for num, fold in enumerate(folds):
    # Find location of the '='
    cmd_point = fold.index("=")
    direction = fold[cmd_point-1]
    fold_line = int(fold[cmd_point+1:])

    m, n = np.shape(paper)

    if direction == "x":
        print(f"Folding along the vertical line x={fold_line}, with paper size {(m, n)}")

        paper = np.logical_or(paper[:, :fold_line-1], paper[:, fold_line:])

    elif direction == "y":
        print(f"Folding along the horizontal line y={fold_line}, with paper size ({m}, {n})")

        paper = np.logical_or(paper[:fold_line-1, :], paper[fold_line:, :])

    print(len(paper[paper == 1]))


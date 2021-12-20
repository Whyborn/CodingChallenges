from get_input import get_data, split_on_lines
import numpy as np
import copy

year, day = 2021, 20

data = get_data(year, day)
# data = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
# #..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
# .######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
# .#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
# .#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
# ...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
# ..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

# #..#.
# #....
# ##..#
# ..#..
# ..###"""

algo, image = data.split("\n\n")

image = [list(line) for line in image.split("\n")]

for line in image:
    print("".join(line))

stages = 2
for _ in range(stages):
    # Create the new image filled with nothing
    new_image = [["." for _ in range(len(image) + 2)] for _ in range(len(image) + 2)]

    # Add the dots at the start and end of each of the image lines
    image = [["."] + line + ["."] for line in image]

    # Create the list of dots that we will use to pad the edges of the image
    filler = ["." for _ in range(len(new_image[0]))]
    image = [filler] + image
    image = image + [filler]

    print("The new image is")
    for line in image:
        print("".join(line))

    # Go through the enhancement process
    count = 0
    for row_num, row in enumerate(new_image):
        for col_num, col in enumerate(row):
            key_string = ""
            test_arr = [["." for _ in range(3)] for _ in range(3)]
            for i_shift in [-1, 0, 1]:
                for j_shift in [-1, 0, 1]:
                    if (row_num + i_shift) < 0 or (row_num + i_shift) >= len(image) or (col_num + j_shift) < 0 or (col_num + j_shift) >= len(image):
                        key_string += "0"
                        test_arr[1 + i_shift][1 + j_shift] = "."
                    else:
                        key_string += "1" if image[row_num + i_shift][col_num + j_shift] == "#" else "0"
                        test_arr[1 + i_shift][1 + j_shift] = image[row_num + i_shift][col_num + j_shift]

            print(f"The array around pixel ({row_num}, {col_num}) is") 
            for line in test_arr:
                print("".join(line))

            print(f"Which corresponds to key {int(key_string, 2)} giving {algo[int(key_string, 2)]}")
            new_image[row_num][col_num] = algo[int(key_string, 2)]
            if new_image[row_num][col_num] == "#":
                count += 1
    print(count)
    print("After enhancement")
    for line in new_image:
        print("".join(line))

    image = copy.deepcopy(new_image)

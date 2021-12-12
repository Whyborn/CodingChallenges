
from get_input import get_data, split_on_lines 
import numpy as np

data = split_on_lines(get_data(2021, 4))

drawn_nums = [int(val) for val in data[0].split(',')]

boards = [np.array([[int(val) for val in row.replace('  ', ' ').split(' ') if (len(val) != 0)] for row in data[i:i+5]]) for i in range(2, len(data), 6)]

# Part 1
# bingo = False

# for i in range(5, len(drawn_nums)):
    # most_recent = drawn_nums[i-1]
    # bingos = set(drawn_nums[0:i])
    # for board in boards:
        # n, m = np.shape(board)
        # for j in range(n):
            # if bingos.issuperset(board[:, j]) or bingos.issuperset(board[j, :]):
                # print("Bingo!")
                # print(board)
                # print(bingos)
                # bingo = True
                # break

        # if bingo:
            # break

    # if bingo:
        # break
            
# unmarked_total = 0
# for y in range(n):
    # for z in range(n):
        # if board[y, z] not in bingos:
            # print(f"{board[y, z]} is not in", bingos)
            # unmarked_total += board[y, z]

# print(unmarked_total * drawn_nums[i-1])

# Part 2
for i in range(5, len(drawn_nums)):
    most_recent = drawn_nums[i-1]
    bingos = set(drawn_nums[0:i])
    flagged_for_removal = []
    for board_num, board in enumerate(boards):
        n, m = np.shape(board)
        for j in range(n):
            if bingos.issuperset(board[:, j]) or bingos.issuperset(board[j, :]):
                print(f"Bingo on board {board_num}!")
                flagged_for_removal.append(board_num)
                break

    print(f"Boards {flagged_for_removal} will now be removed")

    for flag in flagged_for_removal[::-1]:
        board = boards.pop(flag)
            
    print(f"There are {len(boards)} remaining")

    if len(boards) == 0:
        print("No boards left")
        break

unmarked_total = 0
for y in range(n):
    for z in range(n):
        if board[y, z] not in bingos:
            print(f"{board[y, z]} is not in", bingos)
            unmarked_total += board[y, z]

print(unmarked_total * drawn_nums[i-1])


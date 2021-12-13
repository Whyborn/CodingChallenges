from get_input import get_data, split_on_lines

data = [int(val) for val in split_on_lines(get_data(2021, 6))[0].split(',')]

# old_data = data
# for _ in range(80):
    # new_data = []
    # for value in old_data:
        # if value == 0:
            # new_data.append(6)
            # new_data.append(8)
        # else:
            # new_data.append(value-1)

    # old_data = new_data.copy()

# print(len(old_data))

possibles = [0 for _ in range(9)]

for val in data:
    possibles[val] += 1

for _ in range(256):
    new_possibles = [0 for _ in range(9)]
    for i in range(9):
        if i == 0:
            new_possibles[8] = possibles[0]
            new_possibles[6] += possibles[0]

        else:
            new_possibles[i-1] += possibles[i]

    print(possibles)
    possibles = [val for val in new_possibles]

print(sum(possibles))

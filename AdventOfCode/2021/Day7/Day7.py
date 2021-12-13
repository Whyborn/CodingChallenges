from get_input import get_data, split_on_lines

data = [int(val) for val in split_on_lines(get_data(2021, 7))[0].split(',')]

first = True
for pos in range(max(data)):
    total = min(sum([sum(range(1, abs(crab_pos - pos) + 1)) for crab_pos in data]), total) if not first else sum([sum(range(1, abs(crab_pos - pos) + 1)) for crab_pos in data])
    first = False

print(total)

# Day 1 of the Advent of Code challenge 2021

with open("input.txt", 'r') as f:
    count = 0
    for num, line in enumerate(f):

        curr_val = int(line.strip()) 
        if num > 0:
            if curr_val > old_val:
                count += 1

        old_val = curr_val
    print(count)



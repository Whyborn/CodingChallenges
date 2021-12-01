# Part 2 of Day 1 Advent of code 2021

with open('input.txt', 'r') as f:
    
    count = 0
    vals = []
    for line in f:
        vals.append(int(line.strip()))

    for i in range(len(vals) - 3):
        if (sum(vals[i:i+3]) < sum(vals[i+1:i+4])):
            count += 1

    print(count)
    

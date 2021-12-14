from get_input import get_data, split_on_lines
import numpy as np
import copy
import string

year, day = 2021, 14 

data = split_on_lines(get_data(year, day))
# data = split_on_lines("""NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C""")

template = data[0]

pairs, insert = zip(*[line.split(" -> ") for line in data[2:]])

# Construct a dictionary that will count the occurrences of each pair
counter = {}
for pair in pairs:
    counter[pair] = template.count(pair)

steps = 40

# Count the instances of each letter
letter_counter = {letter: template.count(letter) for letter in string.ascii_uppercase}

for _ in range(steps):

    new_counter = copy.deepcopy(counter)

    for pair, letter in zip(pairs, insert):
        letter_counter[letter] += counter[pair]

        if (pair[0] + letter) in counter.keys():
            new_counter[pair[0] + letter] += counter[pair]
        if (letter + pair[1]) in counter.keys():
            new_counter[letter + pair[1]] += counter[pair]

        new_counter[pair] -= counter[pair]

    counter = copy.deepcopy(new_counter)

print(max(letter_counter.values()) - min([val for val in letter_counter.values() if val > 0]))

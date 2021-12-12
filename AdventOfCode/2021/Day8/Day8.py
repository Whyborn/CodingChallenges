from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 8 

data = split_on_lines(get_data(year, day))
print(data)
total = 0
test_str = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]

for line in data:
    # Determine the key for each line
    legend = [0] * 10
    inp, out = line.split("|")
    key_segments = inp.split(" ")
    output_segments = out.split(" ")
    flag_for_removal = []

    for i, rep in enumerate(key_segments):

        # Fill in the known bits
        if len(rep) == 2: # Must be a 1
            legend[1] = rep
            flag_for_removal.append(i)
        elif len(rep) == 3: # Must be a 7
            legend[7] = rep
            flag_for_removal.append(i)
        elif len(rep) == 4: # Must be a 4
            legend[4] = rep
            flag_for_removal.append(i)
        elif len(rep) == 7: # Must be an 8
            legend[8] = rep
            flag_for_removal.append(i)

    for flag in flag_for_removal[::-1]:
        key_segments.pop(flag)

    # Of length 5 strings, only 3 is a superset of 1
    for i, rep in enumerate(key_segments):
        if len(rep) == 5:
            if set(rep).issuperset(legend[1]):
                legend[3] = rep
                key_segments.pop(i)

    # Of the length 6 strings, only 9 is a superset of 3
    for i, rep in enumerate(key_segments):
        if len(rep) == 6:
            if set(rep).issuperset(set(legend[3])):
                legend[9] = rep
                key_segments.pop(i)
                break

    # Of the remaining length 5 strings, only 5 is a subset of 9
    for i, rep in enumerate(key_segments):
        if len(rep) == 5:
            if set(legend[9]).issuperset(set(rep)):
                legend[5] = rep
                key_segments.pop(i)
                break

    # Last length 5 string must be 2
    for i, rep in enumerate(key_segments):
        if len(rep) == 5:
            legend[2] = rep
            key_segments.pop(i)
            break
    
    # If the difference between 8 and the string is in 1, it must be 6
    for i, rep in enumerate(key_segments):
        if len(rep) == 6: # Must be of length 6
            leftover_char = list(set(legend[8]) - set(rep))[0]
            if leftover_char in legend[1]:
                legend[6] = rep
                key_segments.pop(i)
                break

    # Should only be 0 left
    legend[0] = key_segments[0]

    # Now read the output
    out_str = ""
    for out_segment in output_segments:
        for i, key in enumerate(legend):
            if set(out_segment) == set(key):
                out_str += str(i)
                break

    for i, key in enumerate(legend):
        print(f"Number {i} represented by {key}")

    print(out_str)
    total += int(out_str)

print(total)





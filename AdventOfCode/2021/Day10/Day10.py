from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 10 

data = split_on_lines(get_data(year, day))
# data = split_on_lines("""[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""")

opening_chars = ["(", "[", "{", "<"]
closing_chars = [")", "]", "}", ">"]
scores = [3, 57, 1197, 25137]

totals = []

for line in data:
    line_is_valid = True
    valid_chars = ""
    for i in range(len(line)):
        # If its an opening char it's fine
        if line[i] in opening_chars:
            valid_chars += line[i]
        # If its an opening char it might be bad
        if line[i] in closing_chars:
            # Which opening key should it match
            char_key = closing_chars.index(line[i])
            # Does it match? If yes, pop from valid chars
            if opening_chars[char_key] == valid_chars[-1]:
                valid_chars = valid_chars[:-1]
            # It doesn't match
            else:
                total += scores[closing_chars.index(line[i])]
                line_is_valid = False
                break

    if not line_is_valid:
        continue
    else:
        # If we get here, we've reached the end of the line without any invalid characters.
        if len(valid_chars) > 0:
            total = 0
            for char in valid_chars[::-1]:
                total = total * 5 + (opening_chars.index(char) + 1)

            print(valid_chars, total)
            totals.append(total)

totals.sort()
print(totals[int((len(totals) - 1) / 2)])

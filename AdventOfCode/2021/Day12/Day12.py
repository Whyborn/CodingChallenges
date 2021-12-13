from get_input import get_data, split_on_lines
import numpy as np
import string

lower_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)

year, day = 2021, 12 

data = split_on_lines(get_data(year, day))

class Cave:

    def __init__(self, name):

        self.name = name
        self.connected_caves = []

    def add_connection(self, other):

        self.connected_caves += other

class Small_cave:

    def __init__(self, name):
        super.__init__(self, name)
def Part1(data):


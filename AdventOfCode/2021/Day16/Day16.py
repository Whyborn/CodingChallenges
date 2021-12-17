from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 16 

# Today its just a continuous string
data = "{0:08b}".format(int(get_data(year, day), 16))

packets = []

def read_literal_value(data):

while data:
    version = int(data[:3], 2)
    ID = int(data[3:6], 2)

    # Remove them from the string
    data = data[6:]
    if ID == 4:
        # Reading a simple binary number
        count = 0
        num = ""

        while True:
            
            num += str(int(data[5 * count + 1: 5 * (count + 1)]))
            if data[5 * count] == 0:
                break
            count += 1
        

        


    while 

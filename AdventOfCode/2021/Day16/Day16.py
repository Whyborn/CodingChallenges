from get_input import get_data, split_on_lines
import numpy as np

year, day = 2021, 16 

# Today its just a continuous string
data = "{0:08b}".format(int(get_data(year, day), 16))

packets = []

def read_literal_value(data):
    # The first bit of the literal value
    num = data[1:5]

    # Keep track of how many numbers are in this packet, so we can cut off the filler 
    count = 1

    while 1:
        data = [5:]
        num += data[1:5]
        count += 1

        if data[0] == "0":
            data = data[5:]
            break

    # Total bits in the packet so far is the header + the value
    total_bits_in_packet = 6 + 5 * count
    bits_to_chop = total_bits_in_packet % 4
    data = data[bits_to_chop:]

    return int(num, 2)

def read_length_of_packets(data):
    # The 15 bits representing the length of the sub-packets
    length = int(data[:15], 2)
    data = data[15:]

while data:
    version = int(data[:3], 2)
    ID = int(data[3:6], 2)

    # Remove them from the string
    data = data[6:]
    if ID == 4:
        num = read_literal_value(data)
    else:
        length_type_id = data[1:]
        if length_type_id == "0":
            num = read_length_of_packets(data)
        elif length_type_id == "1":
            num = read_number_of_packets(data)

        

        


    while 

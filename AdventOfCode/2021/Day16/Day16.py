from get_input import get_data, split_on_lines
import numpy as np
import string as string

year, day = 2021, 16 

class StringProcessor:
    def __init__(self):
        self.version_count = 0
        
    def read_
# Define the functions
def read_literal_value(data):
    # The first bit of the literal value
    num = data[1:5]

    # Keep track of how many numbers are in this packet, so we can cut off the filler 
    count = 1

    while 1:
        data = data[5:]
        num += data[1:5]
        count += 1

        if data[0] == "0":
            data = data[5:]
            break

    # Total bits in the packet so far is the header + the value
    total_bits_in_packet = 6 + 5 * count
    bits_to_chop = total_bits_in_packet % 4
    data = data[4 - bits_to_chop:]

    return data

def read_length_of_packets(data):
    # First cut off the length type ID
    data = data[1:]

    # The 15 bits representing the length of the sub-packets
    length = int(data[:15], 2)
    data = data[15:]

    # Pass the subpacket as a generic packet
    num = read_generic_packet(data[:length])
    return data

def read_number_of_packets(data):
    # First cut off the length type ID
    data = data[1:]

    # The 11 bits representing the number of sub-packets
    num_packets = int(data[:11], 2)
    data = data[11:]

    # Pass the sub-packet as a generic packet
    for _ in range(num_packets):
        num = read_generic_packet(data)

    return data

def read_generic_packet(data):

    print(f"Input is {data}")
    while data:
        version = int(data[:3], 2)
        ID = int(data[3:6], 2)

        data = data[6:]
        print(f"Version {version} and ID {ID}")

        if ID == 4:
            print(f"Read a literal value- input reads {data}")
            data = read_literal_value(data)
        else:
            length_type_id = data[0]
            if length_type_id == "0":
                print(f"Read a length of packets value- input reads {data}")
                data = read_length_of_packets(data)
            if length_type_id == "1":
                print(f"Read a number of packets value- input reads {data}")
                data = read_number_of_packets(data)

        print(f"After a step, data reads {data}")

# Today its just a continuous string
data = get_data(year, day)
data = "D2FE28"

# Construct the replacement key
keys = [str(i) for i in range(10)] + ["A", "B", "C", "D", "E", "F"]
replace_dict = {char: "{0:04b}".format(int(char, 16)) for char in keys}
data = data.translate(str.maketrans(replace_dict))

read_generic_packet(data)

from math import floor
def solution(n, b):

    # Keep track of the IDs generated
    ID_history = [n]

    # Iterate until we find a duplicate
    while True: 
        
        # Generate x and y
        x, y = sorted(str(n).zfill(4), reverse = True), sorted(str(n).zfill(4), reverse = False)

        # Perform the operation x-y in the desired base
        z = operation_in_base(x, y, b)

        # If ID has previously been generated, exit
        if z in ID_history:
            break
        
        # If not, append it to the list
        ID_history.append(z)
        n = z

    # Return the result
    return len(ID_history) - ID_history.index(z) if len(ID_history) - ID_history.index(z) > 0 else 1

def operation_in_base(x, y, b):

    # Convert the numbers to base 10
    x_b10 = sum(int(coeff) * b ** indx for indx, coeff in enumerate(x[::-1]))
    y_b10 = sum(int(coeff) * b ** indx for indx, coeff in enumerate(y[::-1]))

    # Do x - y in base 10
    z_b10 = x_b10 - y_b10

    # Rebuild z in the desired base
    z = []
    z = ""
    for indx in range(len(x)):
        exponent = len(x) - indx - 1
        if z_b10 >= b ** exponent:
            unit = int(floor(z_b10 / (b ** exponent)))
            z += str(unit)
            z_b10 -= unit * b ** exponent
        else:
            z += "0"

    # Convert back to an integer
    return int(z)

if __name__ == "__main__":

    print(solution(1211, 10))
    print(solution(210022, 3))



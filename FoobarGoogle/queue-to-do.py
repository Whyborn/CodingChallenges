def solution(start, length):

    checksum = 0
    num_queues = 0
    while num_queues < length:
        start_ID = start + length * num_queues
        end_ID = start_ID + (length - num_queues -1)
        checksum ^= XOR(start_ID, end_ID)
        num_queues += 1

    return checksum

def XOR(n, m):
    val = n % 4
    outcomes = [m, 1, m+1, 0]
    if val in [0, 2]:
        return outcomes[(m - n) % 4]
    elif val in [1, 3]:
        return n ^ outcomes[(m - (n + 1)) % 4]
    else:
        return -1

if __name__ == "__main__":
    print(solution(0, 3))

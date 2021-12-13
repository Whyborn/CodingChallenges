import math
import random
import time

def solution(x, y):
    x, y = long(x), long(y)
    num_gens = 0

    #start_time = time.perf_counter()
    while x != y:

        if y > x:
            y -= x
            num_gens += 1
        elif x > y:
            x -= y
            num_gens += 1
        """
        if (time.perf_counter() - start_time) > 5.0:
            print("Test seems to have failed")
            return -1
        """
    return str(num_gens) if x == 1 else "impossible"


def solution2(x, y):
    x, y = long(x), long(y)

    num_gens = 0

    #start_time = time.perf_counter()
    while x != y:
        
        if y > x:
            gen_skips = long(math.floor(y / x))
            if (y % x) == 0:
                gen_skips -= 1
            y -= gen_skips * x
            num_gens += gen_skips
        elif x > y:
            gen_skips = long(math.floor(x / y))
            if (x % y) == 0:
                gen_skips -= 1
            x -= gen_skips * y
            num_gens += gen_skips

        """
        if (time.perf_counter() - start_time) > 5.0:
            print("Test seems to have failed")
            return -1
        """
    return str(int(num_gens)) if int(x) == 1 else "impossible"

if __name__ == "__main__":
    counter = 0
    while True:

        x = int(random.getrandbits(16))
        y = int(random.getrandbits(16))
        if x == 0 or y == 0:
            continue

        #time_1 = time.perf_counter()
        res0 = solution(x, y)
        #time_2 = time.perf_counter()
        if res0 == -1:
            print("Solution(%d, %d) failed" % (x, y))
        #time_3 = time.perf_counter()
        res1 = solution2(x, y)
        #time_4 = time.perf_counter()
        if res1 == -1:
            print("Solution2(%d, %d) failed" % (x, y))
        
        if res0 != res1:
            print(x, y)
            break


        counter += 1

        if (counter % 1000) == 0:
            print("No discrepancies after %d000 tries" % (counter / 1000))

        #if (time_4 - time_3) > (time_2 - time_1):
        #    print("With (%d, %d) v1 is faster" % (x, y))

    """
    print(x, y)
    time_1 = time.perf_counter()
    print(solution(x, y))
    time_2 = time.perf_counter()
    print(solution2(x, y))
    time_3 = time.perf_counter()

    print("Time taken for v1 = %1.3e, time taken for v2 = %1.3e" % ((time_2 - time_1), (time_3 - time_2)))
    """

def solution(num_buns, num_required):

    # The fringe cases
    if num_required == 0:
        bun_list = []
        
        for _ in range(num_buns):
            bun_list.append([])
        return bun_list

    # Everything else
    else:
        key_list = []
        for i in range(2 ** num_buns - 1, 0, -1):
            count, bin_list = count_binary(i)
            if count == (num_buns - num_required + 1):
                while len(bin_list) < num_buns:
                    bin_list.insert(0, 0)

                key_list.append(bin_list)

        bun_list = []
        for _ in range(num_buns):
            bun_list.append([])

        for key_id, key in enumerate(key_list):
            for bun_id, flag in enumerate(key):
                if flag:
                    bun_list[bun_id].append(key_id)

        return bun_list

def count_binary(x):

    bin_as_list = [int(num) for num in list(str(bin(x))[2:])]

    return sum(bin_as_list), bin_as_list

if __name__ == "__main__":

    print(solution(2, 1))
    print(solution(3, 2))
    print(solution(4, 4))
    print(solution(5, 3))
    print(solution(9, 8))

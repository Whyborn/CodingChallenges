def solution(n):

    current_level = 2
    total = 0
    for indx, num in enumerate(range(n)):
        total += num + 1
        if total > n:
            max_level = indx
            break

    num_stairs = 0

    for stair_size in range(1, max_level+1):
        num_stairs += Q(n, stair_size)
    
    return num_stairs - 1

def Q(n, k):

    if (n, k) == (1, 1):
        return 1
    elif n <= k:
        return 0
    elif k < 1:
        return 0
    else:
        term = Q(n-k, k) + Q(n-k, k-1)
        return term
            

if __name__ == "__main__":
    print(solution(50))

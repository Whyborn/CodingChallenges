def solution(n):

    current_level = 2
    total = 0
    for indx, num in enumerate(range(n)):
        total += num + 1
        if total > n:
            max_level = indx
            break

    memory_matrix = [[None for _ in range(max_level)] for _ in range(n)]
    memory_matrix[0][0] = 1
    num_stairs = 0

    for stair_size in range(1, max_level+1):
        num_stairs += Q(n, stair_size, memory_matrix)
    
    return num_stairs - 1

def Q(n, k, mem_matrix):

    if mem_matrix[n-1][k-1] == None:
        
        if ((n > k) and (k >= 1)):
            term = Q(n-k, k, mem_matrix) + Q(n-k, k-1, mem_matrix)
            mem_matrix[n-1][k-1] = term
            return term
        else:
            return 0
            
    else: return mem_matrix[n-1][k-1]

if __name__ == "__main__":
    print(solution(200))

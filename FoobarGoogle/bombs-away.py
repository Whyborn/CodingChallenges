def solution(x, y):
    x, y = int(x), int(y)

    # Find the prime factors of x and y

    prime_factors = [[], []]

    for indx, num in enumerate([x, y]):
        while (num % 2) == 0:
            prime_factors[indx].append(2)
            num /= 2

        for i in range(3, int(pow(num, 0.5)) + 1, 2):

            while (num % i) == 0:
                prime_factors[indx].append(i)
                num /= i

        if num > 2:
            prime_factors[indx].append(num)

    x_factor_set, y_factor_set = set(prime_factors[0]), set(prime_factors[1])

    common_factors = x_factor_set.intersection(y_factor_set)

    if len(common_factors) != 0:
        return "impossible"
    else:
        return common_factors

if __name__ == "__main__":
    print(solution(43, 27))




    

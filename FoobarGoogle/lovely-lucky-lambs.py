def solution(total_lambs):

    if total_lambs <= 2:
        return 0
    
    else:
        # Fibonacci
        t1, t2 = 1, 1
        summation = t1 + t2
        num_fib = 2
        while True:
            t1, t2 = t2, t1 + t2
            print(t1, t2)
            summation += t2
            print(summation)

            if summation > total_lambs:
                break

            num_fib += 1

        # Squares

        num_sqr = 1
        t1 = 1
        summation = 1
        while True:
            t1 *= 2
            print(t1)
            summation += t1

            if summation > total_lambs:
                break
            num_sqr += 1

        return num_fib - num_sqr

if __name__ == "__main__":
    print(solution(10))
    print(solution(143))

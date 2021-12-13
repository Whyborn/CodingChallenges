import math
import decimal as dec
def solution(s):

    # We want the sum of floor(i * sqrt(2) for i in range s)

    s = long(s)

    dec.getcontext.prec = 101
    sqrt2 = dec.Decimal(2).sqrt()
    numer = dec.Decimal(s ** 2 * 2).sqrt()
    denom = dec.Decimal(2 + sqrt2)
    z = long(math.floor(numer))
    m = long(math.floor(numer / denom))

    return str(long(z * (z + 1) / 2. - m * (m + 1) - calc_sum(m, 0)))

def calc_sum(n, total):

    dec.getcontext.prec = 101
    sqrt2 = dec.Decimal(2).sqrt()
    numer = dec.Decimal(n ** 2 * 2).sqrt()
    denom = dec.Decimal(2 + sqrt2)
    z = long(math.floor(numer))
    m = long(math.floor(numer / denom))

    if n <= 0:
        return long(total)
    else:
        return total + z * (z + 1) / 2. - m * (m + 1) - calc_sum(m, total)

minus_sqrt2 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def n1(n):
    return (minus_sqrt2*n)//(10**100)

def s(n):
    if n == 1:
        return 1
        
    if n < 1:
        return 0
    return n*n1(n) + n*(n+1)/2 - n1(n)*(n1(n)+1)/2 - s(n1(n))

def answer(n):
    n = long(n)
    return str(s(n))
    
if __name__ == "__main__":

    print(solution("9812093981230912409172418923710293810938109238109231098231"))
    print(answer("9812093981230912409172418923710293810938109238109231098231"))

    assert(solution("77") == "4208")
    assert(solution("5") == "19")
    #print(solution("77"))
    #print(solution("5"))

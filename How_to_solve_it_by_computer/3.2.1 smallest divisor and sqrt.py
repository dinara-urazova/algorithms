def square_root(m: int):
    error = 0.0001
    g2 = m / 2 # initial guess
    g1 = 0 # next guess
    while abs(g2 - g1) > error:
        g1 = g2 # update previous guess
        g2 = (g1 + m/g1) / 2 # next guess is updated using the avg of the last guess and complement guess
    sqroot = g2
    return sqroot



def smallest_divisor(num: int) -> int:
    divisor = 0
    if num % 2 == 0:
        divisor = 2
        return divisor
    else:
        r = square_root(num)
        d = 3
        while n % d > 0 and d < r:
            d += 2
        if num % d == 0:
            divisor = d
        else:
            divisor = 1
    return divisor




n = 127
res = smallest_divisor(n)
print(res)



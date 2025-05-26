def square_root(m: int):
    error = 0.0001
    g2 = m / 2 # initial guess
    g1 = 0 # next guess
    while abs(g2 - g1) > error:
        g1 = g2 # update previous guess
        g2 = (g1 + m/g1) / 2 # next guess is updated using the avg of the last guess and complement guess
    sqroot = g2
    return sqroot


# while loop
def smallest_divisor(num: int) -> int:
    if num % 2 == 0:
        return 2
    
    r = square_root(num)
    d = 3
    while d <= r:
            if num % d == 0:
                 return d
            d += 2
    return 1



# for loop
def smallest_divisor(num: int) -> int:
    if num % 2 == 0:
        return 2
    else:
        r = num ** 0.5
        for i in range(3, r + 1, 2):
            if num % i == 0:
                return i
        return 1
      

n = 127
res = smallest_divisor(n)
print(res)


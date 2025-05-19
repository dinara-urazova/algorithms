# list of all exact divisors of a certain integer

from typing import List

def all_divisors(num: int):
    if num == 0:
        raise ValueError('Zero has infinitely many divisors')
    num = abs(num)
    divisors = set()

    r = int(num ** 0.5)
    for i in range(1, r + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num/i)
    return sorted(divisors)



num = 125
print(all_divisors(num))

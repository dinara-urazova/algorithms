def all_divisors(num: int):
    if num == 0:
        raise ValueError('Zero has infinitely many divisors')
    num = abs(num)
    count = 0

    r = int(num ** 0.5)
    for i in range(1, r + 1):
        if num % i == 0:
            if i == num // i:
                count += 1
            else:
                count += 2
    return count


def find_smallest_positive_integer(num_of_divisors: int):
    n = 1
    while True:
        if all_divisors(n) >= num_of_divisors:
            return n
        n += 1


n = 7
print(find_smallest_positive_integer(n))
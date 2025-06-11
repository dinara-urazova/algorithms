"""
Find the integer in the range btw 1 and 100 that has the most divisors


"""


def count_divisors(num):
    count = 0
    r = int(num**0.5)
    for i in range(1, r + 1):
        if num % i == 0:
            if i == num // i:
                count += 1
            else:
                count += 2
    return count


def num_with_most_divisors(limit=100):
    max_divisors = 0
    number = 1
    for num in range(1, limit + 1):
        div_count = count_divisors(num)
        if div_count > max_divisors:
            max_divisors = div_count
            number = num
    return number, max_divisors


result_num, result_divs = num_with_most_divisors()
print(
    f"The number between 1 and 100 with the most divisors is {result_num} with {result_divs} divisors."
)

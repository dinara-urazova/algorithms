# design an algorithm that sums digits in a num

def sum_digits(num: int) -> int:
    result = 0
    while num:
        result += num % 10
        num //= 10
    return result

num = 239945
res = sum_digits(num)
print(res)


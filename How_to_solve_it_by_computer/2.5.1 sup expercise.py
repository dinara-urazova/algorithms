# if we're given a certain, num we should compute !0 + !1 ... + !num resulting in a sum of factorials


def sum_of_factorials(n):
    if n < 1:
        return 0

    current_factorial = 1
    total_sum = 0
    for i in range(1, n + 1):
        current_factorial *= i
        total_sum += current_factorial

    return total_sum


n = 5
res = sum_of_factorials(n)
print(res)

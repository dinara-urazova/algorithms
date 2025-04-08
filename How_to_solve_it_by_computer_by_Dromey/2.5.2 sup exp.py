# if we are given a certain num we should compute 1/!0 + 1/!1 ... + 1/!num Sum of factorials but in a denominator, a numerator should always be 1 


def exp(num: int):
    sum = 0
    fact = 1
    for i in range(num + 1):
        if i == 0:
            fact = 1
        else:
            fact = fact * i
        sum += 1 / fact
    return sum


n = 5
res = exp(n)
print(res)

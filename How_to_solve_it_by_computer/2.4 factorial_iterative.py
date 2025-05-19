# iterative approach
def factorial(num: int) -> int:
    res = 1
    for i in range(2, num + 1):
        res *= i
    return res


# built-in function to compute a factorial
import math
def factorial_builtin(n):
    return math.factorial(n)


# recursive approach






"""
Aim: Find the smallest positive integer with at least n divisors.

To compute the number of positive divisors of a number N,
we use its prime factorization:
    N = p1^a1 * p2^a2 * ... * pk^ak
where p1, p2, ..., pk are distinct primes and a1, a2, ..., ak are their exponents.

Each positive divisor of N is formed by choosing an exponent for each prime
between 0 and ai (inclusive), representing how many times that prime appears in the divisor.
Therefore, the total number of positive divisors is:
    (a1 + 1) * (a2 + 1) * ... * (ak + 1)

Example: N = 12 = 2^2 * 3^1

To find all divisors of N, we choose how many times to include each prime factor:
- For 2: exponent choices are 0, 1, 2 → 3 options
- For 3: exponent choices are 0, 1     → 2 options

All possible combinations of exponents give the divisors:

  Exponent of 2   Exponent of 3   Value
  0               0               1
  1               0               2
  2               0               4
  0               1               3
  1               1               6
  2               1               12

Number of divisors = (2 + 1)(1 + 1) = 6
Total number of positive divisors = 3 * 2 = 6
Divisors: 1, 2, 3, 4, 6, 12


This function tries different combinations of prime powers:

 - index = current index in the PRIMES list

 - limit = maximum exponent we’re allowed to use for this prime (so powers are decreasing: 3, then 2, then 1...)

 - current = the number we're building (e.g., 12, 36, etc.)

 - num_divisors = how many divisors the current has so far

 - target = how many divisors we want (minimum)

 - result = stores the smallest number found so far
"""

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def backtrack(index, limit, current, num_divisors, target, result):
    if num_divisors >= target: # base case
        result[0] = min(result[0], current)
        return
    if index >= len(PRIMES):
        return

    prime = PRIMES[index]
    exponent_limit = limit

    for exp in range(1, exponent_limit + 1):
        current *= prime
        if current >= result[0]:
            break
        new_divisors = num_divisors * (exp + 1)
        backtrack(index + 1, exp, current, new_divisors, target, result)


def find_smallest_with_divisors(n):
    result = [float('inf')]
    backtrack(0, 32, 1, 1, n, result)
    return result[0]

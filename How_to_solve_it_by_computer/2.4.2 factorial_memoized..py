
# memoization ( 'turning [the results of] a function into something to be remembered'.)
"""
In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls to pure functions and returning the cached result when the same inputs occur again. In this case we store previously computed values
"""
factorial_cache = {}
def factorial_memoized(num: int) -> int:
    if num in factorial_cache: 
        return factorial_cache[num]
    if num == 0 or num == 1:
        return 1
    result = num * factorial_memoized(num - 1)
    factorial_cache[num] = result
    return result



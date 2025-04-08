def factorial_recursive(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    result = num * factorial_recursive(num - 1)
    return result

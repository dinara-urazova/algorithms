# design an algorithm that reads in a set of n signle digits and converts them into a single decimal integer e.g. {2,7,9,3} to the integer 2793

def digits_into_integer_converter(digits) -> int:
    res = 0
    for dig in digits:
        res = res * 10 + dig
    return res


digits = [2, 7, 9, 3]
res = digits_into_integer_converter(digits)
print(res)

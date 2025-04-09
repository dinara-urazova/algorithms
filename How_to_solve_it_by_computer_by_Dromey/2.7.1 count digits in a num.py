# design an algorithm that counts the number of digits in an integer

def digits_counter(num: int) -> int:
    counter = 0
    while num:
        num  = num // 10
        counter += 1
    return counter




num = 23456
res = digits_counter(num)
print(res)
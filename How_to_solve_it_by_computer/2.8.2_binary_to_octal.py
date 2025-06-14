# convert binary num to octal eg 100100 (36 decimal), octal 44 We cab furst convert bin to decimal and then to octal

def binary_to_octal(bin_num: str) -> int:
    decimal = 0
    exp = len(bin_num) - 1
    for digit in bin_num:
        if digit == '1':
            decimal += 2 ** exp
        exp -= 1
    octal = ''
    while decimal:
        rem = decimal % 8
        octal = str(rem) + octal
        decimal //= 8
    return octal 


bin_num = '100100'
res = binary_to_octal(bin_num)
print(res)
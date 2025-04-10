# turn binary to decimal 

def binary_to_decimal(binary_str: str) -> int:
    
    decimal = 0
    exp = len(binary_str) - 1
    for digit in binary_str:
        if digit == '1':
            decimal += 2 ** exp
        exp -= 1
    return decimal
binary_str = '100111'
res = binary_to_decimal(binary_str)
print(res)




def binary_to_decimal(binary_str: str) -> int:
    decimal_value = 0
    length = len(binary_str)

    for index, digit in enumerate(binary_str):
        if digit == '1':
            decimal_value += 2 ** (length - index - 1)

    return decimal_value

binary_num = "100111"  # Use a string for better clarity
result = binary_to_decimal(binary_num)
print(result)
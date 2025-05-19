"""
convert a decimal integer into a corresponding octal representation

The decimal num eg 275 consists of
2 * 100 + 7 * 10 + 5

5 * 1
7 * 10
2 * 100

275(10) -> 423(8)
3 units -  3 * 1
2 eights - 2 * 8
4 64-s -   4 * 64 
           275 decimal

275(8) 
5 * 1
7 * 8
2 * 64
128 + 56 + 5 = 189(10)

93(10)

num % 2
num = num // 2

q = 93
q = q div 8 -> q = 11 with remainder 5 [1]
q = q div 8 -> q = 1 with remainder 3  [2]
q = q div 8 -> q = 0 with remainder 1  [3]
"""
def base_converter(num: int, base: int) -> str:
    if num == 0:
        return '0'
    
    res = ''
    while num:
        rem = num % base
        if rem >= 10: # convert nums 10-15 to A_F for bases greater than 10
            res = chr(rem - 10 + ord('A')) + res
        else:
            res = str(rem)  + res
        num = num //  base
    return res


num = 36
base = 8
res = base_converter(num, base)
print(res)


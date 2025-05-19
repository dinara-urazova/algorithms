""" 
convert a character  representation of an integer into a decimal representation eg 1984    1  9  8  4 
                                 49 57  56 52 ascii val

ord('9') -> 57 - ord('0') -> 57 - 48 = 9
substract 48 (the ascii val 0) to get an integer

Ok we can extract separate digits, then we would need to construct a decimal number from them see 2.7 alg
decimal = 0
decimal = decimal * 10 + 1
1 * 10 + 9 = 19
19 * 10 + 8 = 198
198 * 10 + 4 = 1984
"""
class Solution():
    def char_to_digit_converter(self, s: str) -> int:
        decimal = 0
        for char in s:
            decimal  = decimal * 10 + (ord(char) - ord('0'))
        return decimal

s = Solution()
num = '1984'
res = s.char_to_digit_converter(num)
print(res)
assert res == 1984
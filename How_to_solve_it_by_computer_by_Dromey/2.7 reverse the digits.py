"""
design an algorithm that accepts a positive integer and reverses the order of its digits

input 27953 = 2 * 10^4 + 7*10^3 + 9*10^2 + 5*10^1 + 3*10^0
Output 35972

We don't know the number of digits so we'd better start with the least significant digit (rightmost digit). We need to chop it off - we want to end with 2795 with the 3 removed and identified.
We can get 2795 by integer division of num by 10 
27953 div 10 -> 2795
This chops off 3 but doesn't allow us to save it. But 3 is the remainder that results from dividing 27953 by 10. To get this remainder we can use mod function

That is 27953 mod 10 -> 3
rem (remainder) = num mod 10 -> rem = 3
num = num div 10 -> num = 2795 and so on so we have the mechanism for iterative accessing the individual digits of the input number.

Next task is to carry the digit reversal
First we get 3 then 5 '35' = 3 * 10 + 5 -> 35
35 * 10 + 9 -> 359 
359 * 10 + 7 -> 3597
3597 * 10 + 2 -> 35972
reversed = prev_value of reversed * 10 + last remainder  - should be eligible for all iteration
[1] rev = rev * 10 + 3 [rev should be 3] to get 3 initial rev should be 0

Last one - condition uder which the iterative process should terminate.
It should be related to the input integer (while there are digits in it as it's reduced by each step) 


Algorithm
1) Use the remainder function to extract the righmost digit of the num
2) increase the prev reversed integer * 10 + add a most recent remainder
3) use integer division by 10 to remove the rightmost digit from the num
"""


class Solution:
    def reverse_digits(self, num: int) -> int:
        reversed = 0
        while num:
            remainder = num % 10
            reversed = reversed * 10 + remainder
            num = num // 10
        return reversed


s = Solution()
assert s.reverse_digits(27953) == 35972
# res = s.reverse_digits(27953)
# print(res)

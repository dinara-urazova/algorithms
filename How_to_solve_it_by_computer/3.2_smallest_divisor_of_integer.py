"""
We have to make up an algorithm to calculate the smallest divisor of a provisioinal num othen than one
One one hand, it's very simple need to go from 2 up to n and try to divide them into num Once they divide, we can terminate
The problem is how to invent a more efficient algorithm
eg num = 36 a set of divisors {2,3,4,6,8,12,18}
an exact divisor of a num divides into that number leaving no remainder
36/4 = 9, 36/9 = 4, 36/4*9 -> 1
Exact divisors of a number must be paired
36 set of divisors (smaller and bigger)
2 * 18
3 * 12
4 * 9
6 * 6
Our algorithm can terminate when we have a pair of factors which correspond to the biggest smaller factor s and the smallest bigger factor b  so that s * b = num; 
s is less than b, the limiting value must occur when s = b when s * s = n
It follows that it's not necessary to look for smallest divisors of n that are greater than the square root of num
This way we could stop the search for a valid exact divisor earlier than we would be able to if the number was prime for example 
eg 127 -> we should only consider candidates such as 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
if the number is even, it's divisible by 2, hence // by 4, 6, 8, 10
if it's odd -> not divisible by 2 or by 4, 6, 8, 10
Algorithm
1) if the num is even, the smallest divisor will be 2
2) compute the square root r of the num
3) while no exact divisor less than square root will do, test next divisor in sequence


1 N is the integer
2 If n is not odd, return 2 as the smallest divisor
else
a) compute the square root r of the n
b) initialize divisor d  = 3
c) while n % d != 0 and d < r, generate next number in odd sequence 
d) if current divisor is the exact divisor of n, then return it
else return 1 as the smallest divisor d of n

"""


def smallest_divisor(num: int) -> int:
    divisor = 0
    if num % 2 == 0:
        divisor = 2
        return divisor
    else:
        r = num ** 0.5
        d = 3
        while n % d > 0 and d < r:
            d += 2
        if num % d == 0:
            divisor = d
        else:
            divisor = 1
    return divisor




n = 127
res = smallest_divisor(n)
print(res)
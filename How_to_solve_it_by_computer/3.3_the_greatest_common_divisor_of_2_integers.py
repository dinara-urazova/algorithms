"""
Euclid algorithm
if x divides a and b, they can be expressed as segments of size x
it means that if a > b, a % b can also be divided by x
if a > b, then b is the upper limit of gcd (greatest common divisor)
if a % b == 0 then b is the gcd
else (if a % b != 0) -> x must be smaller than b and should get into a % b (remember that a % b can be divided by x) 
-> to find gcd(a,b) we should find gcd (b, a % b)

gcd(18, 30) = gcd(12, 18) = gcd(6, 12) gcd = 6

Strategy for the original problem
1) Divide the larger of the 2 numbers by the smaller number
2) If the smaller number exactly divided the larger then it is the gcd
3) Else - remove from the larger number the part common to the smaller number (a % b) and repeat the whole procedure with the new pair of numbers.

r = 30 mod 18 = 12 step (1)
r = 18 mod 12 = 6 step (2)
r = 12 mod 6  = 0  step (3)
6 is the gcd

while gcd not found do
1) get remainder by diving the larger inter by the smaller integer
2) let the smaller integer assume the role of the larger integer
3) let the remainder assume the role of the smaller integer

Algorithm description
1 Establish the 2 positive non-zero integer smaller and larger whose gcd is being sought
2 Repeatedly
a) get the remainder from dividing the larger by the smaller integer
b) let the smaller integer assume the role of the larger integer
c) let the remainder assume the role of the divisor until a zero remainder is obtained
3 Return the gcd
"""
def gcd(a: int, b: int):
    rem = 1
    while rem != 0:
        rem = a % b
        a = b
        b = rem
    return a

res = gcd(18, 30)
print(res)



def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a

res = gcd(18, 30)
print(res)


"""
Generation of the Fibonacci sequence
for n >= 1
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc
new term = preceding term + term before preceding term

a - term bf preceding term
b - preceding term
c - new term

1) Start
a = 0 - first Fibonacci number
b = 1 - second Fibonacci number
c = a + b - third Fibonacci number (first + second)
To generate the fourth number, we need to apply the same definition again.
The 4th Fibonacci is derived from the sum of the second and third Fib nums
The 2nd number has the role of the term before preceding term and the the 3rd Fib number has the role of the preceding term
bp - term before preceding term
p - preceding term

c = a(bp) + b(p)
d = b(bp) + c(p)


Before making the next (4th) computation we must ensure that
1) the new term (3rd) assumes the role of the preceding term
2) what is currently the preceding term must assume the role of the term before preceding term

a = 0       [1] bp
b = 1       [2] p
c = a + b   [3] new term
a = b       [4] bp is previous p
b = c       [5] p is previous new term
a, b = b, c
a, b = b, a + b
From step 5 to step 3 loop
"""


def fib(num: int):
    a = 0
    b = 1
    a = a + b # 1 ( 0 + 1)
    b = a + b

        
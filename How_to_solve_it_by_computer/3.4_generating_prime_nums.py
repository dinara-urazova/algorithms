"""
An algorithm to establish all the primes  in the first n positive integers
A prime num is a positive integer that is exactly divisible only by 1 and itself
THe first few primes are

2 3 5 7 11 13 17 19 23 29 31 37 ...
All primes apart from 2 are odd

How can we establish whether or not a particular number is a prime number
To test it we have to check its divisors eg 13  - 2,3,4,5...12
It would be too tiresome to check all the nums, so we have to minimize the number of nums to check
First, we don't need to examine any even nums apart from
start at 1 and increment +=2
(2), 3, 5, 7, 9, 11 etc
Still, too many
Should observe only prime numbers
Besides no need to check the nums beyond √num (see alg 3.2)
"""
# Python analigue of deomey algorithm

def dromey_primes(n):
    if n < 2:
        return []
    
    primes = [2, 3]
    x = 5 # candidate, we skip even nums and 3
    dx = 2 # to alternate btw 2/4 for odd prime nums like 5-7-11-13-17-19-23 (2-4-2-4- etc) for n >= 5 (6k +/- 1)

    while x <= n:
        is_prime = True

        for p in primes:
            if p * p > x:
                break # we're past root(x)
            if x % p == 0:
                break # not a prime
        
        if is_prime:
            # loop didn't break -> x is prime
            primes.append(x)

        x += dx
        dx = 6 - dx # alternate between 2 and 4
    return primes

print(dromey_primes(30))

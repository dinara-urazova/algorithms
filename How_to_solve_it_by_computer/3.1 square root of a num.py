# alg to find the square root of the number
"""
The method below has actually its name: Newton-Raphson method
the square root n of a certain m number should satisfy the equation
n * n = m (1)

Possible algorithm 
1) Choose the number n < m 
2) Square n and if it's greater than m, decrease it by 1 and repeat step 2
3) If the square of the guess at square root is less than m, we can increase it by 0.1 until we compute the square root
The number of iterations this algorithm requires depends critically on how good our initial guess is.
We need to find a more efficient way which doesn't depend on the initial guess.
e.g. we need to find the square root of 36, choose 9 as an initial guess
9**2 = 81 (more than 36)

Strategy of averaging complementary estimates of the square root
eg 36  - g1 take 9 (9**2 = 81 too high),  36/9 = 4 (4**2 too small) (9+4//2 -> 6 something)
g2 = (g1 + m/g1) / 2
To generate a loop - g1 = g2
How to terminate the process - 


Algorithm descriptioin
1. Establish m the number whose square root is required and the termination condition error e.
2. Set the initial guess g2 to m/2.
3. Repeatedly
a) let g1 assume the role of g2
b) generate a better estimate g2 of the square root using the averaging formula until the absolute difference between g1 and g2 is less than error e.
4. Return the estimated square root g2.
"""

def square_root(m: int):
    error = 0.0001
    g2 = m / 2 # current guess
    g1 = 0 # prev guess
    while abs(g2 - g1) > error:
        g1 = g2 # update previous guess
        g2 = (g1 + m/g1) / 2 # next guess is updated using the avg of the last guess and complement guess
    sqroot = g2
    return sqroot



num = 36
res = square_root(num)
print(res)
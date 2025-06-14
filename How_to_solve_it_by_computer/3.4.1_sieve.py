

# a sample of sive_of_eratosthenes method which seems rather clear


def SieveOfEratosthenes(
    n,
):  # Create a boolean array and initialize all entries it as true.
    # A value in prime[i] will finally be false if i is not a prime, else true.
    prime = [True] * (n + 1)

    for p in range(2, int(n**0.5 + 1)):  # while p * p <= n + 1, on 35 line p += 1
        if prime[p] == True:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False

    # Print all prime numbers
    for p in range(2, n + 1): 
        if prime[p]:
            print(p, end=" ")


n = 30
SieveOfEratosthenes(n)



def modern_sieve(n):
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1): 
        if is_prime[i]: # == True
            # Update all multiples of p
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Print all prime numbers
    return [i for i, prime in enumerate(is_prime) if prime] 
# enumerate(is_prime) -> [(0, False),(1, False)...]

n = 30
modern_sieve(n)
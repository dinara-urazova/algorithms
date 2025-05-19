# Instrumented backtracking to trace calls and returns

def backtrack_trace(index, limit, current, num_divisors, target, result, depth=0):
    indent = '    ' * depth
    print(f"{indent}Entering: index={index}, limit={limit}, current={current}, divisors={num_divisors}, best={result[0]}")
    
    # Base cases
    if num_divisors >= target:
        print(f"{indent}  --> Reached target: updating best from {result[0]} to {current}")
        result[0] = min(result[0], current)
        print(f"{indent}Exiting (base case): index={index}")
        return
    if index >= len(PRIMES):
        print(f"{indent}Exiting (no more primes): index={index}")
        return

    prime = PRIMES[index]
    for exp in range(1, limit + 1):
        current *= prime
        if current >= result[0]:
            print(f"{indent}  Pruning: current {current} >= best {result[0]}")
            break
        new_divisors = num_divisors * (exp + 1)
        print(f"{indent}  Trying {prime}^{exp}: current={current}, divisors={new_divisors}")
        backtrack_trace(index + 1, exp, current, new_divisors, target, result, depth + 1)
    
    print(f"{indent}Exiting: index={index}")
    

def find_smallest_with_divisors_trace(n):
    result = [float('inf')]
    print(f"Starting search for smallest number with >= {n} divisors\n")
    backtrack_trace(0, 32, 1, 1, n, result)
    print(f"\nFinished search. Smallest found = {result[0]}")
    return result[0]

# Constants
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Run trace for n=6
find_smallest_with_divisors_trace(6)
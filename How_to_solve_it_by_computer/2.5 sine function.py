def sin(x):
    term = x  # First term of the series (x^1 / 1!)
    tsin = x  # Initialize tsin with the first term
    i = 1
    error = 10 ** (-6)

    while abs(term) > error:
        i += 2  # Move to the next odd number
        term *= -(x**2) / (i * (i - 1))  # This line calculates the next term
        tsin += term  # Add the new term to tsin

    return tsin


# Example usage
result = sin(4)
print(result)

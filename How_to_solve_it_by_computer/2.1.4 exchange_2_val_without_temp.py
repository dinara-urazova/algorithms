# exchange 2 values not using a temporary variable
a = 100
b = 77
a = a - b
b = a + b
a = b - a
print(f"a = {a}, b = {b}")
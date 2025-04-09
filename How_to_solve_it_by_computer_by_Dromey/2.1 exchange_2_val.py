""" 
Given 2 variables a and b, exchange the values assigned to them

Aim:

new value of a  = old value of b
new value of b = old value of a

a = 721
b = 463
a = b # Step 1: a = b = 463, old value of a (721) is lost
b = a # Step 2: b = 463 (new value of a)

new value of b = new value of a
(b = a = 463, old value of a = 721 is lost)
It means that we should find a way to keep the old value of a and not to lose it, i.e to store value of A in a temporary variable before losing
in Step 1
"""
a = 721
b = 463
print(f"a = {a}, b = {b}")
temp = a # old value is stored in temp
a = b  # a = 463
b = temp # b = 721
print(f"a = {a}, b = {b}")

"""
Algorithm description
1. Save the original value of a in temp.
2. Assign to a the original value of b.
3. Assign to b the original value of a stored in teml variable.

A more common application of this kind of algorithm implies exchange of 2 array elements, e.g. a[i] and a[j]:

temp = a[i]
a[i] = a[j]
a[j] = temp

"""
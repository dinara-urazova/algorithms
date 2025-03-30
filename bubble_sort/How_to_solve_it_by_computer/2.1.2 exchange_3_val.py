# a -> b -> c -> a

a = 721
b = 463
c = 555
print(f"a = {a}, b = {b}, c = {c}")
temp = a # old value is stored in temp
a = b  # a = 463
b = c # b = 555
c = temp # c = 721
print(f"a = {a}, b = {b}, c = {c}")
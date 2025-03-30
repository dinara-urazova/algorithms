# a <- b <- c <- d (+ a -> d)

a = 721
b = 463
c = 555
d = 289
print(f"a = {a}, b = {b}, c = {c}, d = {d}")
temp = d # old value is stored in temp
d = c  # d = c = 555
c = b # c = b = 463
b = a # b = a = 721
a = temp # c = 721
print(f"a = {a}, b = {b}, c = {c}, d = {d}")
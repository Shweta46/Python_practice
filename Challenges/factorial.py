def factorial(n):
    if n > 0 and n > 1:
        return n * factorial(n-1)
    else:
        return 1

l = 5
o = factorial(l)
print(o)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# 1. Base case
# 2. Recursive assumption
# 3. self work
print(factorial(4))

def fibanacci(n):
    if n == 0 or n == 1:
        return n
    return fibanacci(n-1) + fibanacci(n-2) + 1

print(fibanacci(5))

# print the sequence 543212345
def natural(n):
    if n == 1:
        print(1)
        return
    print(n)
    natural(n-1)
    print(n)
print(natural(5))


def even_odd(s):
    if s%2==0:
        print("Even")
    else:
        print("Odd")

def factorial(s):
    if s > 1:
        return s * factorial(s-1)
    else:
        return 1

def prime(s):
    if s > 1:
        n = int(s/2)
        for i in range(2, n):
            if s % i == 0:
                return 0
            else:
                return 1
        return 1
    return 0

def first_prime_n_numbers(s):
    if s > 1:
        for i in range(s):
            for j in range(2, i):
                pass

def leap_year(s):
    if s % 4 == 0:
        return True
    else:
        return False

def binary(s):
    while s > 0:
        s = s // 2

        b.append(s)


s = 2004
print(leap_year(s))
s = 2
even_odd(s)
p = factorial(s)
print(p)
print(prime(s))
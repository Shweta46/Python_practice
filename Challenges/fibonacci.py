def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) + 1

def print_fib(n):
    if n >= 2:
        a = 0
        b = 1
        print(a)
        print(b)
        i = 0
        while(i != n-1):
            l = a + b
            a = b
            b = l
            print(l)
            i = i + 1
    elif n == 0 or n == 1:
        print(0)

n = 6
print(fibonacci(n))
print('Now:')
print(print_fib(n))


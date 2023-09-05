def is_prime( a):
    flag = 0
    if a > 1:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False
    else:
        return False


def primesum(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False

    for i in range(2, n):
        if is_prime[i] and is_prime[n - i]:
            return [i, n - i]

# print(primesum(16777214))


def SieveOfEratosthenes(n, a):
    a = [True for i in range(n + 1)]
    a[0] = a[1] = False
    p = 2
    while p * p <= n:
        if (a[p] == True):
            for i in range(p * p, n + 1, p):
                a[i] = False
        p += 1
    return a

def findPrimePair(n):
    a = [0] * (n + 1)
    a = SieveOfEratosthenes(n, a)
    for i in range(0, n):
        if a[i] and a[n - i]:
            print(i, (n - i))
            return
def prime_sum(n):
    a = [0] * (n+1)
    a = [1 for i in range(n+1)]
    a[0] = a[1] = 0
    p = 2
    while p*p <= n:
        if(a[p] == 1):
            for i in range(p*p, n+1, p):
                a[i] = 0
        p += 1
    print(a)
    for i in range(0, n):
        if a[i] and a[n-i]:
            print(i, (n-i))
            return

n = 10
prime_sum(n)
# a = [0] * (n + 1)
# print(SieveOfEratosthenes(n, a))
findPrimePair(n)
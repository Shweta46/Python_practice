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

print(primesum(16777214))

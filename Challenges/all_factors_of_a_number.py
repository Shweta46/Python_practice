def allFactors(a):
    l = []
    for i in range(1, a+1):
        if a % i == 0:
            l.append(i)
        else:
            continue
    return l

n = 100
print(allFactors(n))
print("More efficient solution: ")

def all_factors(n):
    result = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            result.append(i)

            if n // i != i:
                result.append(n//i)
        i += 1
    result = sorted(result)
    return result

p = 100
print(all_factors(p))
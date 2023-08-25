def allFactors(a):
    l = []
    for i in range(1, a+1):
        if a % i == 0:
            l.append(i)
        else:
            continue
    return l

n = 98145448
# print(allFactors(n))

print("More efficient solution: ")


def isPrime(a):
    l = []
    for i in range(0, a+1):
        flag = 0
        if i > 1:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    flag = 1
                    break
            if flag == 0:
                l.append(i)
    return l

m = 0
n = 10
o = isPrime(n)
print(o)
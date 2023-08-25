def isPrime(l, h):
    for i in range(l, h+1):
        flag = 0
        if i > 1:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    flag = 1
                    break
            if flag == 0:
                print(i)

m = 0
n = 10
o = isPrime(m, n)
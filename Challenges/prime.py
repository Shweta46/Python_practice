def prime(l, u):
    for i in range(l, u + 1):
        if i > 1:
            for j in range(2, int(i/2)+1):
                if (i % j) == 0:
                    break
            else:
                print(i)

m = 0
n = 10
o = prime(m, n)
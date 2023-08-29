def prime_sum(a):
    l = []
    for i in range(0, a + 1):
        flag = 0
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    flag = 1
                    break
            if flag == 0:
                l.append(i)
    l = l[::-1]
    print("The list: ", l)
    p = []
    for i in l:
        print("I am here:", i)
        for j in l:
            print("I am here now:", j)
            print(i+j)
            if i+j == a:
                if i + i == a:
                    p.append(i)
                    if i not in p:
                        p.append(j)

    return p
print(prime_sum(10))


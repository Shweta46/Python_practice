def hundred(n):
    d = [0] * n
    for i in range(0, n-1):
        print("Value of i", i)
        for j in range(0, n):
            print("Value of j:", j)
            if i == 0:
                d[j] = d[j] ^ 1
                print("I am d", d)
                j = 1 + j
                continue
            else:
                # p = i - 1
                d[j-1] = 1 ^ d[j-1]
                print("I am d", d)
                j = i + j
    return d

print(hundred(10))

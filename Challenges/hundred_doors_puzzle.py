def hundred(n):
    s = 2 ** n
    print(bin(s))
    for k in range(1, n+1):
        j = 0
        print("Value of K:", k)
        while(j <= n):
            print("Value of j:", j)
            if k == 1:
                s = (1 << j) ^ s
                print(bin(s))
                j = 1 + j
                continue
            else:
                p = k - 1
                s = (1 << j+p) ^ s
                print(bin(s))
                j = k + j
    return bitExtracted(s, n-1, 1)

def bitExtracted(s, k, p):
    p = ((1 << k) - 1) & (s >> (p-1) )
    print("Answer:")
    return bin(p)

print(hundred(10))


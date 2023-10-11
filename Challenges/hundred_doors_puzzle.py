def hundred(n):
    s = 2 ** n
    for k in range(1, n+1):
        j = 0
        while(j <= n):
            if k == 1:
                s = (1 << j) ^ s
                j = 1 + j
                continue
            else:
                p = k - 1
                s = (1 << j+p) ^ s
                j = k + j
    return bitExtracted(s, n-1, 1)

def bitExtracted(s, k, p):
    p = ((1 << k) - 1) & (s >> (p-1) )
    print("Answer:")
    return bin(p)

print(hundred(100))
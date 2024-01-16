def swapbits(n, i, j):
    p = n >> i
    p = p & 1
    q = n >> j
    q = q & 1
    x = p ^ q
    x1 = x << i
    x2 = x << j
    res = x1 | x2
    number = res ^ n
    print(number)
    return number
def swapbits1(n,i,j):
    p = n >> i # BIT ISOLATION
    q = n >> j
    p1 = p & 1
    q1 = q & 1
    if p1 != q1:
        a1 = 1 << i
        a2 = 1 << j
        num = a1 | a2
        number = n ^ num
        print(number)
        return number
    else:
        print(n)
        return n

# Simply
def swap_bits2(s, i, j):
    if ((s >> i) & 1) == ((s >> j) & 1):
        return s
    else:
        mask = (1 << i) | (1 << j)
        print(mask ^ s)
        return bin(mask ^ s)
n = 9
i = 1
j = 3
swapbits(n, i, j)
swapbits1(n, i, j)
print(bin(n))
print(swap_bits2(n, i, j))
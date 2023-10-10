def print_bits(n, p, q):
    s = str(n)
    l = []
    for i in range(p, q+1, 1):
        i = bin(i)
        i = str(i)
        if i.find(s) != -1:
            l.append(i)
    return l

n = 101
p = 20
q = 30
print(print_bits(n, 20, 30))
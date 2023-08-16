def factors(o):
    l = []
    for i in range(1, o+1):
        if o % i == 0:
            l.append(i)
        else:
            continue
    return l
def gcd(a, b):
    p = factors(a)
    q = factors(b)
    print(p)
    print(q)
    l = []
    for i in range(len(p)):
        for j in range(len(q)):
            if q[j] == p[i]:
                l.append(q[j])
    return max(l)

def gcd1(a, b):
    for i in range(1, min(a, b)):
        if a % i == 0 and b % i == 0:
            g = i
    return g


a = 12
b = 15
# print(gcd(a, b))
print(gcd1(a, b))
m = 8
n = 4
# print(gcd(m, n))

# A MUCH MUCH MUCH EASIER WAY TO DO THIS:




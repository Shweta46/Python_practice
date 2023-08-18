def unique(n):
    l = []
    for i in range(len(n)):
        m = n[i]
        for j in range(i+1, len(n)):
            if m != n[j] and m not in l:
                l.append(m)
    return l

def unique1(n):
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    return l
n = [1,2,4,4,5,3,9,3]
print(unique(n))
print(unique1(n))

def intersection(a1, a2):
    l = []
    for i in a1:
        if (i in a2) and (i not in l):
            l.append(i)
    return l

a1 = [1,2,3,4,5]
a2 = [1,2,5]
print(intersection(a1, a2))


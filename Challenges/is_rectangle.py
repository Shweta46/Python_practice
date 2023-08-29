def solve(A, B, C, D):
    l = [A, B, C, D]
    l = sorted(l)
    if l[0] == l[1] and l[2] == l[3]:
        return 1
    else:
        return 0

print(solve(2,3,2,2))

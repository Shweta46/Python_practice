def solve(A, B, C, D):
    l = [A, B, C, D]
    l = sorted(l)
    print(l[3])

    if l[0] == l[1] or l[0] == l[2] or l[0] == l[3]:
        if l[2] == l[1] or l[2] == l[3]:

            return True
        else:
            return False
    else:
        return False

print(solve(2,3,2,2))

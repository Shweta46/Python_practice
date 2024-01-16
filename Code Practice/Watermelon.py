def funct(s):
    yes = 0
    p = s.split(" ")
    n = len(p)
    print(n)
    # print(p[3])
    for i in range(n):
        if p[i] == '1':
            yes += 1
    print(yes)


l = "1 0 1"
print(funct(l))


def togglebitrange(n, i, j):
    upto = (2**4)-1
    mask = upto << i
    number = n ^ mask
    print(number)
    return number

togglebitrange(21, 1, 4)
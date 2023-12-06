def togglebitrange(n, i, j):
    mask2 = (2 ** (j + 1) - 1)
    mask1 = (2 ** i - 1)
    mask = mask2 - mask1
    number_dash = n ^ mask
    number = number_dash >> i
    print(bin(number))
    print(number)
    return number

togglebitrange(21, 2, 4)
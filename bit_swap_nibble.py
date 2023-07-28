def swapnibble(n):
    x = n & 15
    y = n & 240
    x1 = x << 4
    y1 = y >> 4
    num = x1 | y1
    print(num)
    return num
swapnibble(138)


def reverse_bits(s):
    p = ((s & 0xaaaaaaaa) >> 1) | ((s & 0x55555555) << 1)
    return p

s = 10
print(reverse_bits(s))
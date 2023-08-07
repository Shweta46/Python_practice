def swap(s):
    even = s & 0xAAAAAAAA
    odd = s & 0x55555555
    even = even >> 1
    odd = odd << 1
    p = even | odd
    print(p)
s = 5
s = swap(s)
print(s)
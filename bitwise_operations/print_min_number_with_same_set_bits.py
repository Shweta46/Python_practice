def samebits(n):
    i = n
    while (i > n):
        if count_the_bits(i) == count_the_bits(n):
            return i
        else:
            i += 1

def count_the_bits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

print(samebits(8))
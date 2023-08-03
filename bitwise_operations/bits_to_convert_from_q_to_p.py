def bits(i, j):
    num = i ^ j
    count = 0
    while num:
        num = num & (num - 1)  # clear the least significant bit set
        count = count + 1
    return count

i = 5
j = 12
print(bits(i, j))
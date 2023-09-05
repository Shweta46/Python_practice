def hamming(n1, n2):
    s = n1 ^ n2
    count = 0
    while s:
        if (s & 1 > 0):
            count += 1
        s = s >> 1
    return count

def hammingDistance(a):
    n = len(a)
    count = 0
    for i in range(n):
        # print(a[i])
        for j in range(i+1, n):
            # print(a[j])
            count = count + hamming(a[i], a[j])
            # print(f"Hamming distance of {a[i]} and {a[j]} is: ", count)
    return count*2
a = [ 96, 96, 7, 81, 2, 13 ]

a = [2, 4, 6]
# print(hamming(a))

print(hammingDistance(a))

def hammingDistance2(a):
    n = len(a)
    total_distance = 0
    for bit in range(32):  # Assuming 32-bit integers, you can adjust based on your input
        print("This is bit: ", bit)
        bit_count = 0
        for num in a:
            bit_count += (num >> bit) & 1
        total_distance += bit_count * (n - bit_count)
    return total_distance * 2

a = [96, 96, 7, 81, 2, 13]
print(hammingDistance2(a))
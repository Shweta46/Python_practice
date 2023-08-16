def binary(n, l):
    if n > 0:
        j = n // 2
        binary(j, l)
        print(n % 2)

    else:
        return 0

l = []
p = binary(12, l)

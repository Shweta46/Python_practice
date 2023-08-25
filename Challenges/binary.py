def binary(n):
    if n > 0:
        j = n // 2
        binary(j)
        print(n % 2)
    else:
        return 0

n = 10
binary(n)

print("Another function: ")
def decimal_to_binary(decimal):
    base = ""
    if decimal == 0:
        return 0
    else:
        while decimal != 0:
            base = str(decimal % 2) + base
            decimal //= 2
        return int(base)

print(binary(0))
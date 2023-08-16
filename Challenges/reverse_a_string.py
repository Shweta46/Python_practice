def reverse(n):
    n = n[::-1]
    return n

def reverse2(n):
    str = ''
    for i in n:
        str = i + str
    return str

def reverse3(n):
    n = [n[i] for i in range(len(n)-1, -1, -1)]
    n = "".join(n)
    return n

def reverse4(n):
    if len(n) == 0:
        return n
    else:
        return reverse4(n[1:]) + n[0]

n = "string"
print(reverse(n))
print(reverse2(n))
print(reverse3(n))
print(reverse4(n))
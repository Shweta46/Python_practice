def reverse(s):
    return s[::-1]

def reverse2(s):
    p = ''
    s = str(s)
    for i in s:
        p = i + p
    return p

s = [1,0,9,8,9]
print(reverse(s))
print(reverse2(s))
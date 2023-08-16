def palindrome(n):
    m = len(n)//2
    p = n[:m]
    q = n[m:]
    q = q[::-1]
    for i in range(m):
        if p[i] != q[i]:
            return False
        else:
            continue
    return True

def palindrome2(n):
    m = len(n)
    l = m // 2
    for i in range(l):
        if n[i] != n[m - i - 1]:
            return False
    return True

def palindrome3(n):
    str = ''
    for i in n:
        str = i + str
    if str == n:
        return True
    else:
        return False

a = "strirts"
print(palindrome(a))
print(palindrome2(a))
print(palindrome3(a))
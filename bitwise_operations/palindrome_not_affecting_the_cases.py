def palindrome(s):
    n = s.lower()
    m = len(n)
    l = m // 2
    for i in range(l):
        if n[i] != n[m - i - 1]:
            return False
    return True


print(palindrome("Abba"))
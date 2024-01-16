def binary_(s):
    dict1 = {}
    for i in s:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) + 1

def insert(s):
    n = len(s)
    for i in range(n):
        key = s[i]
        j = i - 1
        while j >= 0 and key < s[j]:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = key

def merge(s):
    if len(s) > 1:
        mid = len(s)//2
        left = s[:mid]
        right = s[mid:]
        merge(left)
        merge(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s[k] = left[i]
                i += 1
            else:
                s[k] = right[i]
                j += 1
            k += 1

        # while i < ilen(left)

def partition(s, low, high):
    pivot = high
    i = low - 1
    for j in range(low, high):
        if s[j] <= pivot:
            s[i], s[j]

    pivot = s[high]
    i = low - 1
    for j in range(low, high):
        if s[j] <= pivot:
            i += 1
            s[i], s[j] = s[j], s[i]
    s[i+1], s[high] = s[high], s[i+1]
    return i+1


def quick(s, low, high):
    if low < high:
        pi = partition(s, low, high)
        quick(s, low, pi - 1)
        quick(s, pi +1, high)

def max_(s):
    m = s[0]
    second = s[0]
    for i in range(len(s)-1):
        if s[i] > m:
            second = m
            m = s[i]
    for i in range(len(s)):
        if s[i] > second and s[i] != m:
            second = s[i]
    return second, m

def gcd1(a,b):
    for i in range(1, min(a, b)):
        if a % i == 0 and b % i == 0:
            g = i
    return g


s= [1, 2,3,40,0,11]
print(max_(s))
print(gcd1(4,16))



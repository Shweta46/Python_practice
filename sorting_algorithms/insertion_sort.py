def insertion_sort(s):
    n = len(s)
    for i in range(n):
        key = s[i]
        j = i - 1
        while j >= 0 and key < s[j]:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = key
    return s

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)



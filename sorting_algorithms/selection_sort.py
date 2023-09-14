def selection_sort(s):
    n = len(s)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if s[j] < s[min]:
                min = j
        s[i], s[min] = s[min], s[i]
    return s

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print(selection_sort(arr))

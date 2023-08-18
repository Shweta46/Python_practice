def merge_sort(s):
    if len(s) > 1:
        mid = len(s)//2
        left = s[:mid]
        right = s[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s[k] = left[i]
                i = i + 1
            else:
                s[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            s[k] = left[i]
            k = k + 1
            i = i + 1

        while j < len(right):
            s[k] = right[j]
            k = k + 1
            j = j + 1
    return s

s = [1, 34, -1, 0, 78]
print(merge_sort(s))
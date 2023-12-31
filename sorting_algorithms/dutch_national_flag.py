def sort_(a):
    n = len(a)
    low = 0
    high = n-1
    mid = 0
    while mid <= high:
        if a[mid] == 0:
            a[mid], a[low] = a[low], a[mid]
            mid += 1
            low += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[high], a[mid] = a[mid], a[high]
            high -= 1
            low += 1
    return a

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(sort_(arr))


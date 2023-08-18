def partition_function(s, low, high):
    pivot = s[high]
    i = low - 1
    for j in range(low, high):
        if s[j] <= pivot:
            i = i + 1
            s[j], s[i] = s[i], s[j]
    s[i+1], s[high] = s[high], s[i+1]
    return i+1

def quick_sort(array, low, high):
    if low < high:
        pi = partition_function(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)







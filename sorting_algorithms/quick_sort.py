def partition_function(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[high] = array[high], array[i+1]
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







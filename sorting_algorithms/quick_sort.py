def partition(s, low, high):
    pivot = s[high]
    i = low - 1
    for j in range(low, high):
        if s[i] <= pivot:
            i = i + 1
            s[j], s[i] = s[i], s[j]
    s[i+1], s[high] = s[high], s[i+1]
    return i+1

def quick(s, low, high):
    if low < high:
        pi = partition(s, low, high)
        quick(s, low, pi - 1)
        quick(s, pi + 1, high)

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quick(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
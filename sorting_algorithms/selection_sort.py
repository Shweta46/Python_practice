# Selection sort in Python
# time complexity O(n*n)
# sorting by finding min_index
def sort(a, n):
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
# selectionSort(arr, size)
sort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)


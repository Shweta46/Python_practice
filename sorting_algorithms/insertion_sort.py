def insertion(s):
    n = len(s)
    for i in range(1,n):
        k = arr[i]
        j = i-1
        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k
arr = [12, 11, 13, 5, 6]
insertion(arr)
print(arr)



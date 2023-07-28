def maxpeak(arr):
    n = len(arr)
    arr2 = []
    for i in range(0, n-2):
        if arr[i] < arr[i+1] and arr[i+1] > arr[i+2]:
            arr2.append(arr[i+1])
    print(arr2)
    maximum = max(arr2)
    print(maximum)
    return maximum

arr = [1,5,6,2,8,12,10]
maxpeak(arr)


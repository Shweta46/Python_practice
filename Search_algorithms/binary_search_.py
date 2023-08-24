def binary_search(s, value):
    high = len(s)
    low = 0
    while low <= high:
        mid = low + (high - low) // 2
        if s[mid] < value:
            low = mid + 1
        elif s[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1

print(binary_search([10,20,30,40,50], 20))
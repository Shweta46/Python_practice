def second_largest_element(s):
    if len(s) < 2:
        return None
    largest = second_largest = -1
    for num in s:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num #to check if the last element is the second largest element or not

    return second_largest

l = [3,3,1,10,23,100, 99]
print(second_largest_element(l))


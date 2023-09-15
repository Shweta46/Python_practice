def occurence(arr, s):
    count = 0
    for element in arr:
        if element == s:
            count += 1
    return count

l = [23,3,1,10,23,100]
print(occurence(l, 23))
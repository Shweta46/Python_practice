def count_elements(n):
    dict1 = {}
    for i in n:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1
l = [1,2,2,3,4,4,4]
print(count_elements(l))
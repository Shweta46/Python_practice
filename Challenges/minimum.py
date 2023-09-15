def minimum_element(s):
    key = s[0]
    for element in s:
        if element < key:
            key = element
    return key

l = [2,3,1,10,23,100]
print(minimum_element(l))
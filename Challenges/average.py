def average(s):
    key = 0
    for element in s:
        key = key + element
    return key/len(s)

l = [2,3,1,10,23,100]
print(average(l))
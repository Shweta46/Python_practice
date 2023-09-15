def remove_duplicates(s):
    l = []
    for element in s:
        if element not in l:
            l.append(element)

    return l

s = [2,2,2,1,1,1,4,5,3,4,5,6]
print(remove_duplicates(s))

# A more efficient way
def remove_duplicates1(s):
    return list(dict.fromkeys(s))

s = [2,2,2,1,1,1,4,5,3,4,5,6]
print(remove_duplicates1(s))

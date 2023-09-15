def maximum(s):
    key = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] < s[j]:
                key = s[j]
    return key

l = [2,3,1,10,23,100]
print(maximum(l))

# more efficient solution

def maximum_element(s):
    if not s:
        return None
    key = s[0]
    for element in s:
        if element > key:
            key = element
    return key

l = [2,3,1,10,23,100]
print(maximum_element(l))

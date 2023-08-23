def isValid(s):
    if len(s) % 2 != 0:
        return False
    dict1 = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for i in s:
        if i in dict1.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if i != dict1[a]: # looking at whether the value of the key is same as i
                return False
    return stack == []
str1 = "{}{)"
print(isValid(str1))
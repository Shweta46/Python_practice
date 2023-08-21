def valid_paranthesis(s):
    count = 0
    for i in s:
        print("THe character right now: ", i)
        if i == "{" or i == "[" or i == "(":
            count += 1
            print('I am here', count)
        elif i == "}" or i == "]" or i == ")":
            count -= 1
            print('And I am here: ', count)
        else:
            return
    if count == 0:
        return True
    else:
        return False

s = "{}{]"
print(valid_paranthesis(s))
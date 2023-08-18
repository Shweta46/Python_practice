def longest_substring(string):
    test = ''
    s=""
    max_length = 0
    if len(string) == 0:
        return 0
    elif len(string) == 1:
        return 1

    for i in list(string):
        current = i
        if current in test:
            test = test[test.index(i) + 1:]
        test = test + i
        if len(test)>max_length:
            s=test[0:]
            max_length = len(s)
            print(s)
    return max_length,s

def longest_substring(a):
    i = 0
    j = 0
    count = 0
    maximum = 0
    dict = {}
    while i < len(a):
        if a[i] not in dict:
            dict[a[i]] = 1
            count += 1
            j = i-1
        else:
            dict.clear()
            # j = i
            count = 0
            dict[a[i]] = 1
        maximum = max(count, maximum)
        i = i + 1
        st = a[j:i]
    return st, maximum

string = "acaaa"
string = "pwwkwe"
# length = longestUniqueSubsttr(string)
length = longest_substring(string)
print(length)


def maximum_subarray(s):
    maximum = 0
    previous_max = 0
    n = len(s)
    i = 0
    while(i < n and maximum >= previous_max):
        previous_max = maximum
        maximum = s[i] + maximum
        i = i + 1
    if maximum < previous_max:
        print(s[i:])
        maximum_subarray(s[i:])

    return maximum

l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray(l))
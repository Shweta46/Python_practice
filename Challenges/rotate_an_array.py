def rotate_array(s, n):
    for i in range(n):
        s.append(s[i])
    del s[:n]
    return s

s = [1,2,4,5,6,7]
print(rotate_array(s, 4))

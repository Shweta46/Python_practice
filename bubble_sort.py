list1 = [1,2,1,1,4,9,0,1]

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
            print(list1)
        else:
            print(list1)
    print( )
print(list1)

def bub(s):
    n = len(s)
    for i in range(n):
        for j in range(0, n-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
            else:
                print(s)
    return s

s = [1,2,1,1,4,9,0,1]
print(s)
print(bub(s))
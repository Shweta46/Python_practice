def set(a, pos):
    r = 1 << pos
    a1 = a | r
    return a1

def reset(a, pos):
    r = 1 << pos
    a2 = a & r
    a3 = a ^ a2
    return a3

def toggle(a, pos):
    a1 = 1 << pos
    return a ^ a1

# toggle, reset, and set the ith bit of the array given that every element is 32 bit.
a = [1,2,3,4,5,31]
pos = 191
i = len(a)
print(i)
element = pos//32
print(a[element])
# for j in range(a[element]):
p1 = pos % 32
print(p1)
position = 32 - p1
print(position)
p = reset(a[element], position)
print(p)



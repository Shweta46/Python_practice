
def bitExtracted(number, k, p):
    return ( ((1 << k) - 1) & (number >> (p-1) ) );

number = 171
print(bin(number))
k = 5
p = 2
print ("The extracted number is ", bitExtracted(number, k, p))

def set(a, pos):
    r = 1 << pos
    a1 = a | r
    return a1

def reset(a, pos):
    r = 1 << pos
    a2 = a & r
    a3 = a ^ a2
    return a3

def swap(n, i, j):
    p = 1 << i
    q = 1 << j
    i = n ^ p
    j = n ^ q
    if(i < 0 and j > 0): #meaning ith bit probably 1 and that jth bit is 0
        n1 = set(n, i)
        n2 = reset(n, j)
        n = n1 | n2
        print(n)
    elif(i > 0 and j < 0):
        n1 = reset(n, i)
        n2 = set(n, j)
        n = n1 | n2
        print(n)
    else:
        print('No swapping needed.')
n = 10
i = 1
j = 2
swap(n,i,j)




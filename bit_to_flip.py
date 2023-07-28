x = 2
y = 10
print(bin(x))
print(bin(y))
n = x^y
count = 0
while n:
    n = n & (n-1)
    count = count+1
print(count)
m = 3
p = 10
number = 10215

binary = bin(number)
binary = str(binary)
n = len(binary)
print(binary)
# print(type(binary))
m = n - m
p = n - p
s = ''
for i in range(p, m):
    print(binary[i])
    s += str(binary[i])
print(s)

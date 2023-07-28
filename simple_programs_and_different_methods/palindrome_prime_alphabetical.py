# Palindrome, sorting, maximum repeated element, class

# PALINDROME:
# 1st method
def palindrome(s):
    n = len(s)
    for i in range(0, int(len(s)/2)):
        if s[i] != s[n-i-1]:
            print('Not one')
    print('Is ')

# 2nd method:
s= 'stet'
palindrome(s)
rev = ''.join(reversed(s))
print(rev)

# 3rd method:
s= "stret"
w = ""
print('FOr the one you didnt do:')
for i in s:
    w = i+w
    print(w)
print('w=',w)

if (s == w):
    print('Yes')
else:
    print('No')

# PRIME NUMBER:
# 1st method:
n = 9
f = 0
for i in range(2,n):
    if (n%i == 0):
        f = 1
        print(f'{n} is not prime number.')
if(f == 0):
    print(f'{n} is prime number.')


# 2nd method
r = int(n**(1/2) + 1)
for i in range(2, r):
    if (n % i == 0):
        f = 1
        print(f'{n} is not prime number.')
if (f == 0):
    print(f'{n} is prime number.')

# 3rd method
from math import sqrt
n1 = int(sqrt(n))
for i in range(2, n1+1):
    if (n % i == 0):
        f = 1
        print(f'{n} is not prime number.')
if (f == 0):
    print(f'{n} is prime number.')

# ALPHABETICAL SORTING:
# 1st method: Turning the string into list and then sorting the list
s = 'geeksforgeeks'
l = []
n = len(s)
for i in range(n):
    l.append(s[i])

for i in range(n):
    for j in range(n-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)

# 2nd method:
s1 = ''.join(sorted(s))
print(s1)

# SORT THE WORDS IN A STRING ALPHABETICALLY
s = 'Hello this is just a program, dont take it so seriously'
for i in s:
    s1 = s.split(" ")
print(s1)

s = s.lower()
for i in s: s1 = s.split(" ")
n = len(s1)
for i in range(1, n):
    min = s1[i]
    j = i - 1
    while(j >= 0 and min < s1[j]):
        s1[j+1] = s1[j]
        j -= 1
    s1[j+1] = min
print(s1)

# ADDING A CHARACTER AT A SPECIFIC POSITION IN A STRING
def insert_character(s, character, index):
    list1 = []
    l = []
    character = [character]
    for i in s:
        l.append(i)
        list1 = l[:index] + character + l[index:]
        print(list1)
    string = ""
    for j in list1:
        string += j
    print(string)
print(insert_character("strng", 'i', 3))



# CONVERTING LIST TO A STRING
# 1st method:
def listtostring(s):
    str1 = " "
    return (str1.join(s))
s = ['geeks', 'for', 'geeks']
print(listtostring(s))

# 2nd method:
def listtostring(s):
    str1 = ' '.join([str(i) for i in s])
    print(str1)
s = ['geeks', 'for', 'geeks', 4]
print(listtostring(s))

# 3rd method:
def listtostring(s):
    str1 = ' '.join(map(str, s))
    print(str1)
s = ['geeks', 'for', 'geeks', 4]
print(listtostring(s))

# SIMPLE IMPLEMENTATION OF STACK USING PYTHON
stack = []
stack.append(10)
stack.append(1)
stack.append(11)
stack.append(12)
stack.append(13)
stack.append(14)
print(stack)
stack.pop()
print(stack)

# MAXIMUM REPEATED ELEMENT
def maximum(s):
    n = len(s)
    l = {}
    # for j in range(n):
    for i in range(0,n):
        if (s[i-1] == s[i]):
            l.append(s[i-1])
    print(l)
    return max(l)
    # l =
s = [11,11,10, 1, 11, 12, 13, 13,13,14, 14]
print(maximum(s))
a = s
data = {item: item for item in a}
# credit Card= 7573060605
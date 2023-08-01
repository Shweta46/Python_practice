def insertion_sort(p):
    a = []
    for i in p:
        a.append(i)
    n = len(a)
    for i in range(n):
        min = a[i]
        j = i -1
        while(j >= 0 and min < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1]=min
    # print(a)
    return a

# ANAGRAM OR NOT
a = "lives"
b = 'elvis'
insertion_sort(a)
is_anagram = lambda x, y: insertion_sort(a) == insertion_sort(b)
print(is_anagram(a, b))

# PALINDROME OR NOT
is_palindrome = lambda a: a == a[::-1]
print(is_palindrome('anna'))

# FACTORIAL
n = 5
factorial = lambda n: n * factorial(n-1) if n > 1 else 1
print(factorial(9))

# LEVENSHTEIN DISTANCE:

# PYTHON TRICK:
# The numerical value 0 is False.
# The empty string '' is False.
# The empty list [] is False.
# The empty set set() is False.
# The empty dictionary {} is False.
# As a rule of thumb, Python objects are considered False if they are empty or zero.

a = "cat"
b = "chello"
c = "chess"
print('This : ')
print(a[0] != b[0])
ls = lambda a, b: len(b) if not a else len(a) if not b else min(ls(a[1:], b[1:]) + (a[0] != b[0]), ls(a[1:], b)+1, ls(a, b[1:])+1)

# There are two trivial cases: if string a is empty, the minimal edit distance is len(b), since you would just need to insert each character of string b. Similarly, if string b is empty, the minimal edit distance is len(a). That means if either string is empty, you can directly return the correct edit distance.
print(ls(a, b))
print(ls(a, c))
print(ls(b, c))

# Caesar’s Cipher Encryption Using Advanced Indexing and list Comprehension

# Here’s the critical part of the code that shows exactly how each character c is shifted by 13 positions:
# abc[(abc.find(c) + 13) % 26]

# First, you find character c’s index in the alphabet abc. Second, you shift the index by adding the integer 13 to character c’s index in the alphabet abc considering our modulo 26 trick (as explained in the previous paragraphs). The result of the one-liner code snippet is the following:

abc = "abcdefghijklmnopqrstuvwxyz"
s = "xthexrussiansxarexcoming"

rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % 26] for c in x])
print(rt13(s))
print(rt13(rt13(s)))

# PRIME NUMBERS IN A RANGE:

prime = lambda x:  for i in range(x) for print('Not prime') if x % i == 0 else 






# Since sets are unordered (and mutable) data structures, the items cannot be accessed through index of key.
s1 = {'apple', 'banana', 'cherry'}
for x in s1:
    print(x)

# and can see if a particular element is present in the set or not
print('banana' in s1)


s = {'a', 'e', 'i', 'o', 'u', 'g', 'e', 'k', 's'}
s.add('f') #append, unlike list, doesnt work with sets
print(s)

s.discard('g')
print(s)

s.remove('a')
print(s)

s.pop()
print(s)

# s.clear()
# print(s)

s2 = {'a', 'e', 'i'}
print(s.difference(s2))

print(s - s2)

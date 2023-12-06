# Adds element to the end of the list
list1 = ['Maths', 'Chem', 1997, 1998, 2, 1, 2, 1, 1, 1, 1]
list1.append(1)
print(list1)

# insert: Adds element to the specific index of the list
list1.insert(1, 2)
print(list1)

# extend:  Add multiple items of an iterable to the end of a list
list2 = [2, 3, 4, -1, 100, 0, -2, -1000]
list1.extend(list2)
print(list1)

# sum: calculates the sum of all elements of the list
print(sum(list2))

# count: counts the number of repetitions of the a given element in the list
print(list1.count(1))

# index: returns the index of the first occurrence
print(list1.index(2))

# min: calculates the minimum of all elements list
print(min(list2))
print(max(list2))

# sort: sorts the elements of the list
list2.sort()
print(list2)

# reverse: reverses a list
list2.reverse()
print(list2[::-1])
print(list2)

# remove: Removes a specific element using its value/ name
list2.remove(-1000)
print(list2)

# pop: Removes an item from a specific index in a list
print(list2.pop()) #prints the popped item of the list
print(list2)
'''
**Question 6:** Write a Python program to combine two dictionaries `dict1` and `dict2` into a new dictionary `combined_dict`, where the keys are unique. If a key exists in both dictionaries, the value from `dict2` should be used. Print the `combined_dict`. 

For example, given `dict1 = {'a': 1, 'b': 2}` and `dict2 = {'b': 3, 'c': 4}`, the `combined_dict` should be `{'a': 1, 'b': 3, 'c': 4}`.
'''
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

def combine(d1, d2):
    combined_dict = {}
    for key, value in d1.items():
        combined_dict[key] = value

    for key, value in d2.items():
        combined_dict[key] = value
    return combined_dict

print(combine(dict1, dict2))

# Shorter program:
def combine2(d1, d2):
    combined_dict = d1.copy()
    combined_dict.update(d2)
    return combined_dict

print(combine2(dict1, dict2))

'''
**Question 7:** Write a Python program to create a dictionary where the keys are numbers from 1 to 5 (both inclusive) and the values are the square of the keys. Print the dictionary.
'''
def square():
    dict1 = {}
    for i in range(1, 6):
        dict1[i] = i**2
    return dict1

print(square())

'''
Question 8: Write a Python program to count the frequency of elements in a list and store it as a dictionary, where the key is the element and the value is the frequency. For example, given the list [1, 2, 1, 3, 2, 1], the dictionary should be {1: 3, 2: 2, 3: 1}. How would you approach this problem?
'''
a = [1, 2, 1, 3, 2, 1]
def frequency(a):
    dict1 = {}
    for i in a:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

print(frequency(a))

'''
Question 9: Write a Python program to find the key with the maximum value in a dictionary. For example, given the dictionary {'a': 10, 'b': 5, 'c': 20}, the program should return 'c'. How would you approach this problem?
'''

b = {'a': 10, 'b': 5, 'c': 20, 'd': 10, 'e': 100, 'f': 12}

def maximum1(d):
    max_ = -9999999
    a = list(d.items())
    l = len(a)
    for i in range(l):
        if a[i][1] > max_:
            max_ = a[i][1]
    for i, j in d.items():
        if j == max_:
            return i

def maximum(d):
    max_val = float('-inf')
    max_key = None
    for key, value in d.items():
        if value > max_val:
            max_val = value
            max_key = key
    return max_key

print(maximum(b))

'''
rite a Python program to merge two dictionaries dict1 and dict2 into a new dictionary merged_dict, where the values of common keys are added together. If a key exists in only one dictionary, its value should be used as-is in the merged_dict. Print the merged_dict.

For example, given dict1 = {'a': 10, 'b': 20, 'c': 30} and dict2 = {'b': 15, 'c': 25, 'd': 35}, the merged_dict should be {'a': 10, 'b': 35, 'c': 55, 'd': 35}.
'''
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 35}

def sum_dict(d1, d2):
    merged_dict = {}
    for key in d1.keys() | d2.keys():
        merged_dict[key] = d1.get(key, 0) + d2.get(key, 0)
    return merged_dict

print(sum_dict(dict1, dict2))

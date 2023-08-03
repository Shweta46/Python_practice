# Accessing the items in the dictionary:

dictionary = {'brand':'Ford', 'year': 1990}
x = dictionary['year']
print(x)

# the same can be done using the get() method
y = dictionary.get('year')
print(y)

# To get the list of keys in the dictionary
s = dictionary.keys()
print(s)

t = dictionary.values()
print(t)

# Sorting a dictionary using the key
def myFunc(e):
    return e['year']

dictionary.sort(key=myFunc)
print(dictionary)


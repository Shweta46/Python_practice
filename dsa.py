# using format option in a simple string
print("{}, A computer science portal for geeks."
      .format("GeeksforGeeks"))

# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))

# formatting a string using a numeric constant
age = 18
print("Hello, I am {} years old !".format(age))

my_string = "{}, is a {} science portal for {}"
list = ["GeeksforGeeks", "computer", "geeks"]
print(my_string.format(*list))

some_text = "There is a %s called %s which %s."
x = some_text % tuple(list)
print(x)

def SquareRoot(x):
    if not isinstance(x, (int, ﬂoat)):
        raise TypeError( 'x must be numeric' )
    elif x < 0:
        raise ValueError( 'x cannot be negative' )
print(SquareRoot(8))

def Sum_of_values(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError( 'parameter must be an iterable type' )
    total = 0
    for v in values:
        if not isinstance(v, (int, ﬂoat)):
            raise TypeError( 'elements must be numeric' )
        total = total+ v
    return total

# print(Sum_of_values(8))

def factors_of(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k
print(factors_of(11))

# def factors(n):
#     results = [ ]
#     for k in range(1,n+1):
#         if n % k == 0:
#             results.append(k)
#         return results
num = '123456'
print(len(num))

# n=int(input("Enter number:"))
# count=0
# while(n>0):
#     count=count+1
#     n=n//10
# print("The number of digits in the number are:",count)

r = 190
ro = r//11
print(ro)

n = 10
# result = foo(n if n >= 0 else -n)

class Parrot:
    # class attribute
    species = "bird"
 # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
# access the class attributes
print("Blu is a {}".format(Parrot.species))
print("Woo is also a {}".format(Parrot.species))
# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

f = 101;
print(f)
# Global vs.local variables in functions
def someFunction():
    global f
    print(f)
    f = "changing global variable"
someFunction()
print(f)

#Typecasting array to list:

import array
arr = array.array("i", [1, 2, 3, 4, 5])
lst = arr.tolist()
print(type(lst)) # <class 'list'>
print(lst)

# Reverse a list

x=[1,2,3,4,5,6,7]
x.reverse()
print(x)

# Sorts the elements in ascending order
x=[7, 6, 5, 4, 3, 2, 1]
x.sort()
print(x)

# Count ():Returns the number of times a specified value occurs in a tuple
x=(1,2,3,4,5,6,2,10,2,11,12,2)
print(x.count(2))

x = (1,2,3,4,5,6,2,10,2,11,12,2)
y = len(x)
print(y)

# We cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# Some of the basic set operations are:
# • Add()
# • Remove()
# • Len()
# • Item in x
# • Pop
# • Clear
x={1,2,3}
x.update([4,5],[6,7,8])
print(x)

# List Operations:
# • Del()
# • Append()
# • Extend()
# • Insert()
# • Pop()
# • Remove()
# • Reverse()
# • Sort()

#****************************************************************************************************************************************
# Creating an array in Python
from array import *
array1 = array('i', [10,20,30,40,50])
for x in array1:
    print(x)
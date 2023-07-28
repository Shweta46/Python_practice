list1 = [1,2,3,4,4,1,3,5]
list2 = []
list1.sort()
print(list1)

# Without the sort function
l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]
print('This is the updated list: ', l)

# Sorting the alphabets
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True) #for reverse order of vowels
print('Sorted list: ', vowels)

# Sort list using key
def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=takeSecond)
print(random)


import string
print('Alphabet from a-z')
for letter in string.ascii_lowercase:
    print(letter, end='')
print('Alphabet from A-Z')
for letter in string.ascii_uppercase:
    print(letter, end='')

# class Stack:
#   def __init__(self, size=10):
#       self._stack = []
#       self._size = size
#
#   def is_empty(self):
#       return len(self._stack) <= 0
#
#   def push(self, data):
#       if len(self._stack) >= self._size:
#           raise Exception('Stack overflow')
#       else:
#           self._stack.append(data)
#
#   def pop(self):
#       if len(self._stack) <= 0:
#           raise Exception('Stack underflow')
#       else:
#           return self._stack.pop()
#
#   def peek(self):
#       if len(self._stack) <= 0:
#           raise Exception('Stack underflow')
#       else:
#           return self._stack[-1]
#
#   def length(self):
#       return len(self._stack)
#
#
# stack = Stack(5)
# stack.push(5)
# stack.push(2)
# stack.push(3)
# stack.push(9)
# stack.push(6)
# print(stack.peek())
# print(stack.pop())
# print(stack.length())
# print(stack.peek())
#
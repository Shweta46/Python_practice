# CREATING A DICTIONARY USING LIST COMPREHENSION:
import time

r = ' .Hello world.  '
print(r)
a = r.rstrip()
print(a)

print([{x: y} for x in range(3) for y in range(3)])

employees = {'Alice': 10000,
            'Bob': 99817,
            'Carol': 122908,
            'Frank': 133000}

top_earners = []
for key, value in employees.items():
    if value >= 100000:
        top_earners.append((key, value))
print(top_earners)


knights = {'Mock': 1, 'Night':2, 'Tight': 3, 'Okay':4}
for k, v in knights.items():
    print(k, v)

# LIST COMPREHENSION: [EXPRESSION + CONTEXT].
# Context: It defines which list elements to select.
# Expression: it defines how to modify each list element before adding the result to the list.
# The square brackets indicate that the new element is a list.

# LEVELS INTO COMPLEXITY:

# LEVEL 1
y = [x*x for x in range(10)]
print(y)

# LEVEL 2
print([[x, y] for x in range(3) for y in range(3)])

# LEVEL 3
print([x ** 2 for x in range(10) if x % 2 > 0])

top = [(k, v) for k, v in employees.items() if v > 100000]
print(top)

# LEVEL 4

s = "You are\nMy Fire\nThe one\nDesire"
# split string by newline
ls = s.split("\n", maxsplit=1)
print(ls)

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
w = [[x for x in line.split() if len(x) > 3] for line in text.split('\n')]

# The above code line creates a list within a list.
# 1st list is split on the basis of \n, so each line is a separate element is the outer list.
# 2nd list has the line again split and the words selected have more than 3 characters.
p = ([x for x in text.split() if len(x) > 3])
print(p)
print(w)

# ***************************************************************************************************************************************************
# FILE OPERATIONS:
start = time.time()
# filename = 'dictionary.py'
# f = open(filename)
# lines = []
# for line in f:
#     lines.append(line.strip())
# print(lines)

# OR the above code line can be written as:
print([lines.strip() for lines in open('dictionary.py')])
end = time.time()
time1 = 1000 * (end - start)
print(time1)

# ***************************************************************************************************************************************************

# LAMBDA WITH MAP FUNCTION:

txt1 = ['lambda functions are anonymous functions.',
'anonymous functions dont have a name.',
'functions are objects in Python.']
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt1)
print(list(mark))

marks = [(True, txt1[i]) if 'anonymous' in txt1[i] else (False, txt1[i]) for i in range(len(txt1))]
print(marks)

# ***************************************************************************************************************************************************

# SLICING: x[start:stop:step].
# Note: If the stop argument is given, the respective position is
# excluded from the slice.

s = 'Eat more fruits!'
print(s[6:1:-1])

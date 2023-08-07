
# 1. Treating functions as objects:

def shout(text):
    return text.upper()
print(shout('Hello'))
yell = shout
print(yell('Hello'))

# In the above example, we have assigned the function shout to a variable.
# This will not call the function instead it takes the function object referenced by a shout and creates a second name pointing to it, yell.

# 2. Passing the function as an argument
def shout(text):
    return text.upper()
def whisper(text):
    print("Lower text")
    return text.lower()
def greet(func):
    greeting = func('Hi, I am created by a function passed as an argument.')
    print(greeting)

greet(shout)
greet(whisper)

# 3. RETURNING FUNCTIONS FROM ANOTHER FUNCTION:
def create_adder(x):
    def adder(y):
        # print(x)
        return x+y
    return adder
# add_15 = create_adder(15)(10)
# print(add_15)
# The functon create_adder, when run, returns a function adder. This returned function can be interpreted as:
# add_15 = adder(y)
# Now, we assign the argument to add_15 as:
add_15 = create_adder(15)
print(add_15(10))

# THE ABOVE CODING LINES CAN ALSO BE WRITTEN AS:
# add_15 = create_adder(x)(y)
# print(add_15)

# **********************************************************************************************************************************************
# DECORATORS:

def hello_decorator(func):
    print('Hello, this is before function execution.')
    def inner1():
        print('Hello, this is during function execution.')
        func()
        print('This is after function execution.')
    return inner1
def function_to_be_used():
    print('This is inside the function.')

function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()

# THE ABOVE CODE LINES ARE TO BE INTERPRETED AS:

# function_to_be_used() = hello_decorator(function_to_be_used)
# this makes func = function_to_be_used()
# then, hello_decorator() will return the inner1 function.
# This makes:
# function_to_be_used = inner1()
# So, when finally function_to_be_used is called, its like calling the inner1 function.
# This triggers the function inside the hello_decorator and returns the print statement of inner1 and then func (which became equal to function_to_be_used) then last after execution print statement.

#
# def add(f):
#     def inner():
#         return f() + 64
#     return inner
# def foo():
#     return 5
# foo = add(foo)
#
# print(foo())
# THE USE OF KEYWORD "@_DECORATOR"
def add(f):
    def inner():
        print('hi')
        return f() + 64
    return inner
@add
def foo():
    return 5

# THE CODE LINES @add
# def foo() translates to: foo = add(foo)

print(foo())
def print_(n):
    if n == 0:
        return
    print_(n-1)
    print(n)

def print_2(n):
    if n > 0:
        print_2(n - 1)
        print(n)

print(print_(10))
# print(print_2(10))

'''
HEAD VS TAIL RECURSION:
function()
{
    i) return condition
    ii) task
    iii) call 
    1, 2, 3, 4, ...............
}

if : call, and then task
then the answer is reversed 10, 9, 8, 6 ........
'''
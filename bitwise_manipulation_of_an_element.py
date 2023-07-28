def set(a, pos):
    r = 1 << pos
    a1 = a | r
    print(a1)

def reset(a, pos):
    r = 1 << pos
    a2 = a & r
    a3 = a ^ a2
    print(a3)

def toggle(a, pos):
    a1 = 1 << pos
    print(a ^ a1)

a = int(input('Enter the number'))
pos = int(input('Enter the position'))
set(a, pos)

reset(a, pos)
toggle(a, pos)
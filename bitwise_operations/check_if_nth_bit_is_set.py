def set_or_not(s, pos):
    if((s >> pos) & 1):
        return True
    else:
        t = s ^ (1 << pos)
        return t
def unset_the_bit(s, pos):
    p = s & (~(1 << pos))
    return p

def toggle(s, pos):
    s = s ^ (1 << pos)
    return s

n = 5
p = 1
print(set_or_not(n, p))
print(unset_the_bit(n, p))
print(toggle(n, p))
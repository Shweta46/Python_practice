# num = number, pos = position at which we want to set the bit
def set(num, pos):
    # First step = Shift '1'
    # Second step = Bitwise OR
    num |= (1 << pos)
    print(num)


num, pos = 6, 1
set(num, pos)

# TO TOGGLE THE DIGIT ON NTH POSITION
def toggle(num, pos):
# First Step: Shifts '1'
# Second Step: XOR num
    num ^= (1 << pos)
    print(num)


num1, pos1 = 1, 1

toggle(num1, pos1)

# TO SEE IF THE SIGN OF A NUMBER IS NEGATIVE OR POSITIVE, IF YES PRINT -1, OR 1
v = -20
print(v)
sign = (v > 0) - (v < 0)
print("Sign is:", sign)

# TO CHECK IF THE SIGN OF TWO NUMBERS IS DIFFERENT OR SAME
x = -7
y = 2
sign = ((x^y)<0)
print(sign)

# SWAPPING TWO NUMBERS WITHOUT A THIRD VARIABLE
a = 3
b = 2
a = a + b
b = a - b
a = a - b
print(a,b)

a = 3
b = 2
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

# TO SEE IF A NUMBER IS A POWER OF 2 NUMBER. E.G., 2,4,8,16,ETC
v = 17
if (v & (v-1)) == 0:
    print("True")
else:
    print("Nope")

# TO NEGATE AN INTEGER VALUE
p = 20
print(bin(p))
p = ~p
print(p)
# the NOT of a number:
# ~3 = -4
# ~20 = -21
# To make it 20, we add 1 to the whole number
p = p + 1
print('Negative p is:', p)

# TO CHECK IF AN INTEGER IS EVEN OR ODD
t = 110
print(True) if (t & 1) else print(False)

# TO GET THE LARGER OR SMALLER OF TWO INTEGERS WITHOUT BRANCHING
x = 9
y = 10
r = x < y
print("Larger is:", r)

# TO NEGATE NUMBERS USING BITWISE OPERATIONS
x = 5
y = ~x
y = y+1
print(y)

# COUNT THE NUMBER OF 1'S IN THE BINARY REPRESENTATION OF A NUMBER

# MULTIPLY THE NUMBER WITH TWO USING BITWISE OPERATIONS
r = 10
r = r<<1
print(r)

# DIVIDE THE NUMBER BY 2
r = 10
print(r>>1)

# MULTIPLY THE NUMBER  BY 4 AND DIVIDE BY 4
r = 80
print(r<<2, r>>2)

# FETCH THE BIT AT iTH POSITION FROM THE LEFT
r = 51
pos = 3
bit = 1 << pos
print("Position of bit:", bin(bit))
print(1) if (r & pos) else print(0)

i = 100
print(bin(i))

# TOGGLE ALL THE BITS OF A NUMBER:
x = 10
x = x^1
print(x)

def toggleBitsFromLToR(n, l, r):
    # 'num' having 'r'
    # number of bits and bits in the range l to r are the only set bits
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)
    # toggle bits in the range l to r in 'n'
    # Besides this, we can calculate num as: num=(1<<r)-l and return the number
    return (n ^ num)
n = 50
l = 2
r = 5
print(toggleBitsFromLToR(n, l, r))


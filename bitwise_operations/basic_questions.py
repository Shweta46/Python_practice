def set_the_bit(s, pos):
    p = s | (1 << pos)
    return p

def clear_a_bit(s, pos):
    p = s & ~(1 << pos)
    return p

def inverting_a_bit(s, pos):
    p = s ^ (1 << pos)
    return p

def extract_bits_within_a_range(s, p1, p2):
    mask2 = (2**(p2+1) - 1)
    mask1 = (2**p1 - 1)
    mask = mask2 - mask1
    p_dash = s & mask
    p = p_dash >> p1
    return p

def calculate_hemming_weight(s):
    count = 0
    while s:
        if (s & 1 == 1):
            count += 1
        s = s >> 1
    print("The hemming weight of this:")
    return count

def power_of_two(s):
    p = (s - 1) & s
    if p == 0:
        return True
    else:
        return False

def bits_required_to_convert_a_to_b(s, t):
    p = s ^ t
    count = 0
    while p:
        if p & 1 > 0:
            count += 1
        p = p >> 1
    return count

def swap_bits_in_given_locations(s):
    pass

a = 15
print(bin(a))
print(set_the_bit(a, 2))
print(clear_a_bit(a, 3))
print(inverting_a_bit(a, 0))
print(extract_bits_within_a_range(a, 1, 3))
print(calculate_hemming_weight(a))
print(power_of_two(a))
print(bits_required_to_convert_a_to_b(a, 26))
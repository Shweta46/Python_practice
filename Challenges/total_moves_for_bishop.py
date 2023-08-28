def solve(A, B):
    if A == 1 or B == 1 or A == 8 or B == 8:
        return 7
    elif A == 2 or B == 2 or A == 7 or B == 7:
        return 9
    elif A == 3 or B == 3 or A == 6 or B == 6:
        return 11
    else:
        return 13

def solve(A, B):
    max_row = 4
    max_column = 4
    col_left = B - 1
    col_right = max_row - B
    row_up = A - 1
    row_down = max_column - A

    a = min(col_left, row_up)
    b = min(col_left, row_down)
    c = min(col_right, row_up)
    d = min(col_right, row_down)
    ans = a + b + c + d
    return ans

def bishop_fucking_moves(a, b):
    max_i = 3
    max_j = 3
    count = 0
    a1 = a
    b1 = b
    while a1 < max_i and b1 < max_j:
        count += 1
        a1 += 1
        b1 += 1

    a1 = a
    b1 = b
    while a1 < max_i and b1 > 1:
        count += 1
        a1 += 1
        b1 -= 1

    a1 = a
    b1 = b
    while a1 > 1 and b1 < max_j:
        count += 1
        a1 -= 1
        b1 += 1

    a1 = a
    b1 = b
    while a1 > 1 and b1 > 1:
        count += 1
        a1 -= 1
        b1 -= 1

    return count

print(bishop_fucking_moves(1, 3))

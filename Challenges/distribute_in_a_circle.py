def solve(A, B, C):
    effective_start = (C - 1) % B
    position = (effective_start + A) % B
    return position

print(solve(8, 5, 2))
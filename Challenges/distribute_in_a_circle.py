def solve(A, B, C):
    effective_start = (C - 1) % B
    position = (effective_start + A) % B
    return position

def distribute(A, B, C):
    return (A+C-1)%B

print(solve(8, 5, 2))
print(distribute(8, 5, 2))
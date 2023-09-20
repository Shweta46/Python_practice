def ways_to_reach(i, j, size):
    if i == size-1 and j == size-1:
        return 1
    if i == size or j == size:
        return 0
    z = ways_to_reach(i+1, j+1, size)
    x = ways_to_reach(i+1, j, size)
    y = ways_to_reach(i, j+1, size)
    return x+y+z

print(ways_to_reach( 0, 0, 4))
def ways_to_reach(grid, i, j, size):
    if i == size-1 and j == size-1:
        return 1
    if i == size or j == size:
        return 0
    if grid[i][j] == -1:
        return 0
    x = ways_to_reach(grid, i+1, j, size)
    y = ways_to_reach(grid, i, j+1, size)
    return x+y

weight = [[0, 0, 0],
          [-1, 0, 0],
          [0, 0, 0]]

i = 0
j = 0
size = 3
print(ways_to_reach(weight, i, j, size))
def ways_to_reach(weight, i, j, size):
    if i == size-1 and j == size-1:
        return weight[i][j]
    if i == size or j == size:
        return float('inf')
    x = ways_to_reach(weight, i+1, j, size)
    y = ways_to_reach(weight, i, j+1, size)
    return weight[i][j] + min(x, y)
    # here, weight[i][j] is added to account for the weight of the block we started with

i = 0
j = 0
size = 3
# weight = [[1, 2, 3],
#         [4, 5, 6],
        # [7, 8, 9]]

weight = [[4, 4, 16],
          [2, 7, 20],
          [7, 8, 9]]
print(ways_to_reach(weight, i, j, size))


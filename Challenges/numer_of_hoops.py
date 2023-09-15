def reachTarget(target):
    target = abs(target)
    sum = 0
    step = 0
    while sum < target or (sum - target) % 2 != 0:
        step = step + 1
        sum = sum + step
    return step

target = 2
print(reachTarget(target))


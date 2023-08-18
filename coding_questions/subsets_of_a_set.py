def powerset(s):
    x = len(s)
    x = len(s)
    for i in range(1 << x):
        print ([s[j] for j in range(x) if (i & (1 << j))])
s = [4, 5, 6]
powerset(s)

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

def get_powerset(a):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(a) == 0:
        return [[]]

    subsets = []
    first_element = a[0]
    remaining_list = a[1:]
    # Strategy: get all the subsets of remaining_list. For each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_element
    for partial_subset in get_powerset(remaining_list):
        subsets.append(partial_subset)
        subsets.append(partial_subset[:] + [first_element])
    return subsets

print(list(powerset(s)))
# print(list(get_powerset(s)))
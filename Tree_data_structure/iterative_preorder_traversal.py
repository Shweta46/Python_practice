class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def isIdentical(x, y):
    if x is None and y is None:
        return True
    if x is None:
        return False
    if y is None:
        return False

    stack = deque()
    stack.append((x, y))

    while stack:
        x, y = stack.pop()
        if x.key != y.key:
            return False
        if x.left and y.left:
            stack.append((x.left, y.left))
        elif x.left or y.left:
            return False
        if x.right and y.right:
            stack.append((x.right, y.right))
        elif x.right or y.right:
            return False
    return True

x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

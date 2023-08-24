class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def node_present(root, key):
    if root is None:
        return False

    if root.data is key:
        return True

    res1 = node_present(root.right, key)

    if res1:
        return True

    res2 = node_present(root.left, key)
    return res2

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)

key = 6
if node_present(root, key):
    print("Yes")
else:
    print("No")

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def inorder(self, l, root):
        if root:
            self.inorder(l, root.left)
            l.append(root.data)
            self.inorder(l, root.right)
        return l

    def preorder(self, l, root):
        if root:
            l.append(root.data)
            self.inorder(l, root.left)
            self.inorder(l, root.right)
        return l

    def postorder(self, l, root):
        if root:
            self.inorder(l, root.left)
            self.inorder(l, root.right)
            l.append(root.data)
        return l

    def identical(self, root1, root2):
        list1 = []
        list2 = []
        p1 = self.inorder(list1, root1)
        q1 = self.inorder(list2, root2)
        print(p1)
        print(q1)

        p2 = self.preorder(list1, root1)
        q2 = self.preorder(list2, root2)
        print(p2)
        print(q2)

        p3 = self.postorder(list1, root1)
        q3 = self.postorder(list2, root2)
        print(p3)
        print(q3)
        if p1 == q1 and p2 == q2 and p3 == q3:
            print("Identical.")
            return True
        else:
            print("Not identical.")
            return False

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right= Node(5)
root1.right.right= Node(6)
root1.right.left= Node(7)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right= Node(5)
root2.right.right= Node(6)
root2.right.left= Node(7)
t1 = Tree()

t1.identical(root1, root2)

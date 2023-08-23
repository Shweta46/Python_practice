class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printlist(self):
        if self.left:
            self.left.printlist()
        print(self.data)
        if self.right:
            self.right.printlist()

root = Node(12)
root.insert(6)
root.insert(12)
root.insert(3)
root.printlist()
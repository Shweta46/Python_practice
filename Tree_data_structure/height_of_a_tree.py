class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def insert(self, data):
        if data:
            if data < self.data:
                self.left = self.left(root.data)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def height(self, root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max(left, right) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right= Node(5)
root.right.right= Node(6)
root.right.left= Node(7)

t = Tree()
print("Preorder: ")
t.preorder(root)
print("\nInorder: ")
t.inorder(root)
print("\nPostorder: ")
t.postorder(root)
print("\nHeight of tree: ")
print(t.height(root))


# def preorder_stack(self,root):
#     p=[]
#     st=[]
#     if root==None:
#         return p
#     st.append(root)
#     while(len(st)!=0):
#         root=st.pop()
#     # print(root.data)
#     p.append(root.data)
#     if(root.right!=None):
#         st.append(root.right)
#     if(root.left!=None):
#         st.append(root.left)
#     # print(p)
#     return p

# def inorder_stack(self,root):
#     p=[]
#     st=[]
#     node=root
#     while(True):
#         if node!=None:
#             st.append(node)
#             node=node.left
#         else:
#             if len(st)==0:
#                 break
#             node=st.pop()
#             p.append(node.data)
#             node=node.right
#         return p


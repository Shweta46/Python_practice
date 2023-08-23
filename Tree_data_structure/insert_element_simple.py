class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data, end=" ")

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

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
root.left.right = Node(5)

t = Tree()
t.inorder(root)
t.preorder(root)
t.postorder(root)

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


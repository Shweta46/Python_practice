class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node =  Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def middle_of_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        # slow = slow.next
        return slow.data

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

link = linkedlist()
link.push(1)
link.push(2)
link.push(3)
link.push(4)
link.push(5)
link.push(6)
link.print_ll()
print("The middle of the node is:")
print(link.middle_of_node())

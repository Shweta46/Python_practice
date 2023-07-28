# Python program to detect and remove loop in linked list

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def identifyCycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                self.removeCycle(slow)
                print('Loop detected.')
        print('No loop.')

    def removeCycle(self, slow):
        curr = self.head
        while curr:
            ptr = slow
            while ptr.next is not slow and ptr.next is not curr:
                ptr = ptr.next
            if ptr.next == curr:
                ptr.next = None
                return
            curr = curr.next
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next


# Driver program
llist = LinkedList()
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.printList()
# llist.delete_node(0)
print('After deletion:')
llist.head.next.next.next = llist.head.next
llist.identifyCycle()
print("Linked List after removing loop")
llist.printList()


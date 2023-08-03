class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def sort_without_sort_function(self):
        current = self.head
        index = None
        if current is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next
                current = current.next
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = linkedlist()
llist.push(11)
llist.push(1)
llist.push(10)
llist.push(9)
llist.push(7)
llist.push(0)
llist.push(2)
llist.printlist()
print('Unsorted list: ')
llist.sort_without_sort_function()
print('The sorted list is: ')
llist.printlist()
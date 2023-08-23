class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def duplicates(self):
        current = self.head
        l = []
        while current is not None:
            if current.data not in l:
                l.append(current.data)
            current = current.next
        print(l)
        self.head = None
        l = l[::-1]
        for i in l:
            self.push(i)

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(2)
llist.push(2)
llist.push(1)
llist.push(5)
llist.printlist()
llist.duplicates()
print("After removing duplicates:")
llist.printlist()



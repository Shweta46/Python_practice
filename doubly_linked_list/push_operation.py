class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublylinkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        self.head.next = new_node
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

dlist = doublylinkedlist()
dlist.push(12)
dlist.push(13)
dlist.push(14)
dlist.push(15)
dlist.push(16)
dlist.printlist()
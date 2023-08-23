class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    def deletenode(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return 0
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        t2 = temp.next.next
        temp.next = None
        temp.next = t2

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = linkedlist()
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.printlist()
llist.deletenode(0)
print('List after deletion:')
llist.printlist()











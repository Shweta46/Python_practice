class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def deletion(self, value):
        temp = self.head
        if temp is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == value:
                break
            prev1 = temp
            temp = temp.next
        if temp is None:
            return
        prev1.next = temp.next
        temp.next.prev = prev1
        temp = None

    def deletion_using_position(self, pos):
        temp = self.head
        if temp is None:
            return
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        t2 = temp.next.next
        # temp.next = None
        temp.next = t2
        t2.prev = temp

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = linkedlist()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.printlist()
llist.deletion(2)
print("After deletion: ")
llist.printlist()
print("Specific data: ")
print(llist.head.next.next.next.prev.data)
























        

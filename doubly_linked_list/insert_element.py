class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Doublyll:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete_value(self, value):
        temp = self.head
        if temp is None:
            return
        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp.next.prev = prev
        temp.next = None

    def delete_pos(self, pos):
        temp = self.head
        if temp is None:
            return
        if pos == 0:
            self.head = temp.next
            temp.next.prev = None
            temp = None
        for i in range(pos - 1):
            if temp is None:
                break
            temp = temp.next
        if temp is None:
            return
        t2 = temp.next.next
        t2.prev = temp
        temp.next = None
        temp.next = t2

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = Doublyll()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.printlist()
llist.delete_pos(0)
print("After deletion: ")
llist.printlist()
print("Specific data: ")
print(llist.head.next.prev.data)
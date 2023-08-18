class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        temp = self.head
        if temp is None:
            return
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = linkedlist()
llist.push(2)
llist.push(21)
llist.push(3)
llist.push(5)
llist.push(90)
llist.printlist()
llist.delete(22)
print("The new list:")
llist.printlist()
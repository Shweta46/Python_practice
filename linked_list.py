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

    def delete(self, key):
        temp = self.head
#         if the head has the key element
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
#         if the element is in the middle then keep track of the previous node
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
        temp = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = linkedlist()
llist.push(90)
llist.push(9)
llist.push(10)
llist.push(80)
llist.push(40)
llist.push(10)

llist.printlist()
llist.delete(10)
print('New linked list')
llist.printlist()











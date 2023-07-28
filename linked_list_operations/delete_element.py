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

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
    def delete_pos(self, pos):
        temp = self.head
        if temp is None:
            return
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos-1):
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
    def detect(self):
        fast = self.head
        slow = self.head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                print('loop exists. ')
                self.remove1(slow)
                return True
        print('loop doesnt exist.')
        return False
    def remove1(self, slow):
        p2 = slow
        p1 = slow
        count = 1
        while p1 != p2:
            count = count + 1
            p1 = p1.next

        p1 = self.head
        p3 = self.head


        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        while p2.next != p1:
            p2 = p2.next
        p2.next = None

    def reversed(self):
        current = self.head
        prev = None
        next_one = None
        while current is not None:
            next_one = current.next
            current.next = prev
            prev = current
            current = next_one
        self.head = prev

    def printlink(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = linkedlist()
llist.push(0)
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.printlink()
# llist.head.next.next.next.next.next = llist.head.next
# llist.detect()
# llist.print()
if(llist.detect()):
    print("Loop Found")
llist.reversed()
# llist.delete_node(7)
# llist.delete_pos(5)
# print('After deletion:')
llist.printlink()













































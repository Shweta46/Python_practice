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

    def reverse(self, slow):
        current = slow
        prev = None
        next1 = None
        while current is not None:
            next1 = current.next
            current.next = prev
            prev = current
            current = next1
        slow = prev
        return slow
    def palindrome(self):
        fast = self.head
        slow = self.head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        print('Data: ', slow.data)
        current = slow
        prev = None
        next1 = None
        while current is not None:
            next1 = current.next
            current.next = prev
            prev = current
            current = next1
        slow = prev
        q = self.head
        count = 0
        # Follow one pointer and conclude the program, dont compare two pointers, they never have the same address.
        while slow is not None:
            if q.data == slow.data:
                count += 1
            else:
                return False
            q = q.next
            slow = slow.next
        return True

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = linkedlist()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(3)
llist.push(2)
llist.push(1)

print('The list')
llist.printlist()
if llist.palindrome():
    print('Palindrome.')
else:
    print('Not palindrome. ')
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

    def palindrome(self):
        temp = self.head
        l = []
        while temp is not None:
            l.append(temp.data)
            temp = temp.next
        print(l)
        p = l[::-1]
        i = 0
        while i < len(l):
            if l[i] == p[i]:
                i += 1
                continue
            else:
                return False
        return True

    def isPalindrome(self, head):
        rev = None
        # Slow pointer
        slow = head
        # Fast pointer
        fast = head
        # Until the first half keep reversing the nodes
        while fast and fast.next:
            # Keep moving in double speed
            fast = fast.next.next
            # Keep reversing the node
            slow_next = slow.next
            slow.next = rev
            rev = slow
            slow = slow_next
        # In case lenght of linkedlist is odd
        if fast:
            slow = slow.next
        # Compare the elements
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

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
llist.isPalindrome()
if llist.palindrome():
    print('Palindrome.')
else:
    print('Not palindrome.')
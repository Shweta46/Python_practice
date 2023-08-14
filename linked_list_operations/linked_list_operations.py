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

    def delete_element(self, key):
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
        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return

        t2 = temp.next.next
        temp.next = None
        temp.next = t2

    def delete_node_wo_head(self, pos):
        if pos is None:  # If linked list is empty
            return
        elif pos.next is None:
            print("This is last node, require head, can't be freed\n")
            return

        # copy data of the next node to current node
        pos.data = pos.next.data

        # perform conventional deletion
        pos.next = pos.next.next

    def delete_last_occurence_of_key_from_list(self, key):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == key:
                special = temp
            temp = temp.next
        print('Special print:')
        print(special.data)

        temp = self.head
        while temp.next != special:
            temp = temp.next
        temp.next = special.next
        # special = None

    # def eliminate_duplicates_from_the_list(self):
    #     temp = self.head
    #     while temp is None:
    #         p1 = temp.data
    #         while (temp.data == p1):

    def detect_loop(self):
        fast = self.head
        slow = self.head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                print('loop')
                self.remove_loop(slow)

    def remove_loop(self, pos):
        p1 = self.head
        p2 = pos
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        while p2.next != p1:
            p2 = p2.next
        p2.next = None

    # another way
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


    def rotate_the_link_to_the_front_by_k_nodes(self, k):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        p2 = temp
        p1 = self.head
        if k > 0:
            for i in range(1, k):
                p1 = p1.next
            p2.next = self.head
            self.head = p1.next
            p1.next = None
        else:
            return
    def reverse(self):
        current = self.head
        prev = None
        next_one = None
        while current is not None:
            next_one = current.next
            current.next = prev
            prev = current
            current = next_one
        self.head = prev
    def print_the_middle(self, start, end):
        temp = self.head
        if temp is None:
            return
        count = 0
        for i in range(start):
            if temp is None:
                break
            temp = temp.next

        for i in range(end+1):
            print(temp.data)
            temp = temp.next

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = linkedlist()
llist.push(2)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(2)
llist.push(1)
llist.printlist()
llist.delete_element(3)
# del_node = llist.head.next
# llist.delete_node_wo_head(del_node)
# llist.delete_pos(2)
# llist.rotate_the_link_to_the_front_by_k_nodes(2)
# llist.head.next.next.next.next.next = llist.head.next
# llist.detect_loop()
# llist.reverse()
llist.delete_last_occurence_of_key_from_list(2)
# llist.rotate_the_link_to_the_front_by_k_nodes(3)
print('New list: ')
llist.printlist()
# llist.print_the_middle(0, 4)





















































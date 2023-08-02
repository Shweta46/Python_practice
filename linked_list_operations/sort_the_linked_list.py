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

    def bub_sort(self, list):
        n = len(list)
        for i in range(n):
            min = list[i]
            j = i - 1
            while j >= 0 and min < list[j]:
                list[j + 1] = list[j]
                j -= 1
            list[j+1] = min
        return list
    # Use merge sort instead o decrease the time complexity of the program


    def sort_list(self):
        temp = self.head
        l = []
        while temp is not None:
            l.append(temp.data)
            temp = temp.next
        print(l)
        self.bub_sort(l)
        print('Sorted list: ')
        print(l)
        self.head = l[0]
        for i in range(1, len(l) - 1):
            self.push(l[i])
        print(l)
        return l


    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = linkedlist()
llist.push(11)
llist.push(1)
llist.push(10)
llist.push(9)
llist.push(7)
llist.push(0)
llist.push(2)
llist.printlist()
llist.sort_list()
print('The sorted list is: ')
llist.printlist()
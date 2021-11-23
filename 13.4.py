class Node:

    def __init__(self, item):

        self.item = item
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add_start(self, item):

        node = Node(item)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def del_start(self):

        if self.head.next is not None:
            self.head.next.prev = None
        self.head = self.head.next

    def output(self):   # вывод

        current = self.head
        while current:
            print(current.item)
            current = current.next

    def add_end(self, new):
        node = Node(new)
        if self.head is not None:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur
        else:
            self.head = node

    def del_end(self):
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None

    def del_before(self, key):
        cur = self.head
        while cur.next.item != key:
            cur = cur.next
        if self.head == cur:
            self.head = cur.next
        else:
            cur.prev.next = cur.next
        cur.next.prev = cur.prev

    def add_before(self, key, new):
        node = Node(new)
        cur = self.head
        while cur.item != key:
            cur = cur.next
        if cur != self.head:
            cur.prev.next = node
        else:
            self.head = node
        node.prev = cur.prev
        cur.prev = node
        node.next = cur

    def searh(self, key):
        current = self.head
        while current is not None:
            if current.item == key:
                return True
            current = current.next
        return False




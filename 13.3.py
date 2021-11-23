#   реализация односвязного списка
class Node:     # класс узла

    def __init__(self, item):
        self.item = item
        self.next = None    # указатель на след узел
class LinkedList: # класс списка

    def __init__(self):

        self.head = None    # объект первого узла (изначально он пуст)

    def is_empty(self):

        return self.head is None

    def output(self):   # вывод
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def add(self, item):    # добавление в начало

        node = Node(item)   # создаем обект класса Node со значением item
        node.next = self.head   # указывет на первый узел
        self.head = node    # теперь первый узел это node

    def delite(self):    # удаление головного   ̶м̶о̶з̶г̶а̶ узла

        self.head = self.head.next

    def del_after_key(self, key):

        current = self.head
        while current.item != key:
            current = current.next
        current.next = current.next.next

    def add_after_key(self, key, new):

        current = self.head
        while current.item != key:
            current = current.next
        node = Node(new)
        node.next = current.next
        current.next = node
    def searh(self, key):
        current = self.head
        while current is not None:
            if current.item == key:
                return True
            current = current.next
        return False


    #   приколюха
    # def __call__(self, index):
    #
    #     curr_index = 0
    #     current = self.head
    #     while curr_index < index:
    #         current = current.next
    #         curr_index += 1
    #     return current.item


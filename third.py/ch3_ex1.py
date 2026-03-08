class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    def insert(self, index, value):
        # 1. Check bounds
        if index < 0 or index > self._size:
            raise ValueError("Index out of bounds")

        new_node = Node(value)

        # 2. Insert at the beginning
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node

            # If list was empty, tail also becomes new node
            if self.tail is None:
                self.tail = new_node

            self._size += 1
            return

        # 3. Insert at the end
        if index == self._size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self._size += 1
            return

        # 4. Insert in the middle
        current = self.head
        for _ in range(index):
            current = current.next

        previous = current.prev

        new_node.prev = previous
        new_node.next = current

        previous.next = new_node
        current.prev = new_node

        self._size += 1

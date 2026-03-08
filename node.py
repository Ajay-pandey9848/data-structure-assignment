class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

def print_nodes(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'value: {self.value}'

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return f'H: {self.head}'

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        print(f'self now: {self}')
        if node is not None:
            while node.get_next() is not None:
                self.add_to_head(node.next_node.value)
                self.reverse_list(node.next_node, None)
                return self.head.value
            return node.value

l = LinkedList()
l.add_to_head(1)
l.add_to_head(2)
l.add_to_head(3)
l.add_to_head(4)
l.add_to_head(5)
print(l.head.value)  # should be 5
l.reverse_list(l.head, None)
print(l.head.value)  # should be 1

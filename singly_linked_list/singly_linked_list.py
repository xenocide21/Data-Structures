class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length = 0

    def __str__(self):
        pass

    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = Node(value, None)

            self.head = new_tail
            self.tail = new_tail

        else:
            new_tail = Node(value, None)

            old_tail = self.tail
            old_tail.next = new_tail

            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.length = self.length - 1
            return current_head.value

    # def remove_tail(self):
    #     if not self.tail:
    #         return None
    #     if self.tail == self.head:
    #         current_tail = self.tail
    #         self.tail = None
    #         self.head = None
    #         self.length -= 1
    #         return current_tail.value
    #     else:
    #         current_node = self.head
    #         while current_node.next != self.tail:
    #             current_node.next
    #         old_tail = current_node.next.value
    #         current_node.next = None
    #         self.tail = current_node
    #         self.length -= 1
    #         return old_tail

    def remove_tail(self):
        if not self.head:
            return None
        if self.head == self.tail:
            current_tail = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return current_tail.value
        else:
            current_node = self.head
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()
            new_current_tail = self.tail.get_value()
            self.tail = current_node
            self.tail.set_next(None)
            return new_current_tail

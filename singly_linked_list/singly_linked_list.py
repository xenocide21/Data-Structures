class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # The next node in the list


class LinkedList:
    def __init__(self):
        self.head: Node = None  # points to the first node in the list
        self.tail: Node = None  # Points to the last node in the list
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

    def remove_tail(self):
        if not self.tail:
            return None

        if self.tail == self.head:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return current_tail.value
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node.next
            old_tail = current_node.next.value
            current_node.next = None
            self.tail = current_node
            self.length -= 1
            return old_tail

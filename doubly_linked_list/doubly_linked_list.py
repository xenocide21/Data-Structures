"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        else:
            value = self.head.value
            self.length -= 1
            if self.tail is self.head:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        else:
            value = self.tail.value
            self.length -= 1
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if not node:
            return
        if self.head is self.tail:
            return
        if node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = self.head
        self.head = node
        node.prev = None

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if not node:
            return
        if self.head is self.tail:
            return
        if node is self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = self.tail
        node.prev.next = node
        self.tail = node
        node.next = None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if not node:
            return None
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node is self.head:
                self.head = node.next
            if node is self.tail:
                self.tail = node.prev
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        head = self.head
        if not head:
            return 0
        max_val = head.value
        while head.next:
            if head.value > max_val:
                max_val = head.value
            head = head.next
        if head.value > max_val:
            max_val = head.value
        return max_val

def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node #sets tail to the next node
        self.tail = new_node #adds tail to that node
    self.length += 1
    return True 
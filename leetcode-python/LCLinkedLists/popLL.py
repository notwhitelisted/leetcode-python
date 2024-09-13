def pop(self):
    #for pop, need tail to point to previous next value of the node, then POP that thang off, return node
    if self.length == 0:
        return None
    temp = self.head
    pre = self.head
    while(temp.next):
        pre = temp
        temp = temp.next
    #when false, run this
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
        self.head = None
        self.tail = None
    return temp #returns node that we removed
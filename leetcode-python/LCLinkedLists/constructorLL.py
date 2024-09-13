"""class LinkedList:
    def __init__(self, value): #create node + initialize new linkedlist
    
    def append(self, value): #create new node + add node to end

    def prepend(self, value): #create new node + add node to beginning

    def insert(self, index, value): #create new node + insert node
"""
class Node: 
    #new node 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    #constructor
    def __init__(self, value):
        new_node = Node(value) #creates the node
        self.head = new_node #head points to new node
        self.tail = new_node #tail points to new node
        self.length = 1 #starting #

    #print_list method
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #append method 
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

# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.print_list()

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
        #return temp.value

# my_linked_list = LinkedList(1)
# my_linked_list.append(2)

# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())

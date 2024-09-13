#method to go through values of linked list
def print_list(self):
    temp = self.head
    while temp is not None: #when temp var doesn't = None, run the below code
        print(temp.value) #print out the value of each
        temp = temp.next #then move temp var to next node for the next value 
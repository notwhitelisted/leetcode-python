#Classes
class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('pink')

print('Cookie one is now', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

"""
class LinkedList:
    def __init__(self, value): constructor function

    other functions within the class 
    def append(self, value): 
    def pop(self):
    def prepend(self, value):
    def insert(self, index, value):
    def remove(self, index):
"""

#Pointers 
num1 = 11 #num1 point to 11 somewhere in memory addy
num2 = num1 #num2 point to the same 11 in the memory addy

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1)) #both point at the same memory
print("num2 points to:", id(num2)) #both point at the same memory

#Now adding new value to num2
num2 = 22
print("\nAfter num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

print("\nnum1 points to:", id(num1)) #points to same point in memeory
print("num2 points to:", id(num2)) #points to dfifferent point in memory 

#once a value is in place in memory, it cannot be changed

dict1 = {
    'value': 11
}
dict2 = dict1 #point at the same dictionary memory

print("before vlaue is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

#what if value of dict2 is 22
dict2['value'] = 22
print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) #both point to the same memory addy

"""
So why are they different in this instance? dictionaries can change values
integers are immutable and cannot be changed. 

this is important because linkedlist nodes operating like dictionary
so 2 var pointing at the same node, the var continue to point at same node
can change where var are pointing. can change head to point to new node. 

no var pointing to a value, it will be removed to make space 


"""
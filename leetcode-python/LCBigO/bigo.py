"""
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)
"""

#pass in # of n, ran n times. order of operations
#straight line, linear, proportional 

"""def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)
print_items(10)"""
 
#pass in n * n = n^2 - for i and j
#another for loop within the function, but not within each other 
#is just n 

def add_items(n):
    return n + n

#n operations dependent on what operations is used
#if n is just addition, then it is O(1)



#different terms for input - 2 parameters = O(a) + O(b) = O(a + b)
def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)


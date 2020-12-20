# Educational code to try to understand the implementation of the linked lists data structure.

# Creating the node class:

class node:
    def __init__(self, data=None, nexto=None):
        self.data = data
        self.nexto = nexto


# Creating the linked list class:

class linked_list:
    
    # Constructor:
    def __init__(self):
        self.head = None
        
        # When a new instance of the linked_list class gets instantiated, it only creates an empty linked list.
    
    # Method to add a node to the front of the linked list:
    def add_front(self, data):
        self.head = node(data=data, nexto=self.head)
        
        # The new node gets added and it will point to the node before it. So if we add the following numbers in the following order to the list: ``4, 5, 6, 7, 8' then 8 will be the first element of the list and it will point to 7, which will point to 6, which in turn will point to 5, which points to 4, which will be the end of the list and point to None.
        
    def add_end(self, data):
        if self.is_empty():
            self.head = node(data=data, nexto=None)
        else:
            new_node = node(data=data, nexto=None)
            self.head.nexto = new_node
            self.head = new_node 
    
#         if self.head:
#             self.head.data = data
#             self.head.nexto = node(data=data, nexto=None)
#         else:
#             self.head = node(data=data, nexto=None)
            
    def is_empty(self):
        return self.head == None
        
        
        
# ##########################################
# TESTING TIME
# ##########################################

# Making a decorator function to separate the two testing functions.

def decor(func):
    print("\n", 50*"#", "\n")
    func()
    print("\n", 50*"#", "\n")




my_llist = linked_list() # Instantiating a new linked list object.


# Testing add_front() method:

def testing_front():
    print("TESTING add_front() METHOD\n")
    print("The first my_llist.head =", my_llist.head)
    
    my_llist.add_front(4)
    print("my_llist.head after adding '4' to the front of the llist:", my_llist.head)
    print("my_llist.head.data after adding '4' to the front of the list:", my_llist.head.data)
    print("my_llist.head.nexto after adding '4' to the front of the list:", my_llist.head.nexto)
    
    print("\n")
    my_llist.add_front(5)
    print("my_llist.head after adding '5' to the front of the llist:", my_llist.head)
    print("my_llist.head.data after adding '5' to the front of the llist:", my_llist.head.data)
    print("my_llist.head.nexto after adding '5' to the front of the llist:", my_llist.head.nexto)
    
    print("\n")
    my_llist.add_front(6)
    my_llist.add_front(7)
    my_llist.add_front(8)
    print(my_llist.head)
    print(my_llist.head.data)
    print(my_llist.head.nexto)

def testing_end():
    print("TESTING add_end() METHOD\n")
    print("The first my_llist.head =", my_llist.head)
    
    my_llist.add_end(4)
    print("my_llist.head after adding '4' to the end of the llist:", my_llist.head)
    print("my_llist.head.data after adding '4' to the end of the list:", my_llist.head.data)
    print("my_llist.head.nexto after adding '4' to the end of the list:", my_llist.head.nexto)
    
    print("\n")
    my_llist.add_end(5)
    print("my_llist.head after adding '5' to the end of the llist:", my_llist.head)
    print("my_llist.head.data after adding '5' to the end of the llist:", my_llist.head.data)
    print("my_llist.head.nexto after adding '5' to the end of the llist:", my_llist.head.nexto)
    
    print("\n")
    my_llist.add_end(6)
    print("my_llist.head after adding '6' to the end of the llist:", my_llist.head)
    print("my_llist.head.data after adding '6' to the end of the llist:", my_llist.head.data)
    print("my_llist.head.nexto after adding '6' to the end of the llist:", my_llist.head.nexto)
    
    print("\n")
    my_llist.add_end(7)
    my_llist.add_end(8)
    print(my_llist.head)
    print(my_llist.head.data)
    print(my_llist.head.nexto)



# decor(testing_front)
decor(testing_end)

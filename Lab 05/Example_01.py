# Define a Node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        # Each node has a piece of data and a reference to the next node
        self.data = data
        self.next = None

# Define a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        # Initialize the head of the list to None
        self.head = None
        
    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        
        # If the list is empty, set the new node as the head of the list
        if self.head is None:
            self.head = new_node
            return
        
        # If the list is not empty, traverse to the end of the list and add the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
        # Traverse the list starting from the head and print each node's data
        current_node = self.head
        while current_node:
            print("[",current_node.data,", ",current_node," ]")
            current_node = current_node.next
    
# Create a new linked list and append some nodes
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.print_list()

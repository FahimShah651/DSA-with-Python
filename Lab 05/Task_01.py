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
        
    def add_node(self, data):
        # Create a new node with the given data
        new_node = Node(data)

        # If the list is empty, set the new node as the head of the list
        if self.head is None:
            self.head = new_node
            return
        
        # If the list is not empty, insert the new node after the first node
        first_node = self.head
        new_node.next = first_node.next
        first_node.next = new_node
        
    def delete_node(self):
        # If the list is empty, do nothing
        if self.head is None:
            return
        
        # If the list has only one node, set the head to None
        if self.head.next is None:
            self.head = None
            return
        
        # If the list has multiple nodes, traverse to the second-to-last node and set its next to None
        second_last_node = self.head
        while second_last_node.next.next:
            second_last_node = second_last_node.next
        second_last_node.next = None
        
    def print_list(self):
        # Traverse the list starting from the head and print each node's data
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Create a new linked list and append some nodes
my_list = LinkedList()
my_list.append(11)
my_list.append(12)
my_list.append(13)

# Print the initial list
print("Initial list:")
my_list.print_list()

# Add a new node after the first node
my_list.add_node(14)
print("After adding a node:")
my_list.print_list()

# Delete the last node
my_list.delete_node()
print("After deleting a node:")
my_list.print_list()

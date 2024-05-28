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
        
        # If the list is empty, set the new node as the head of the list and make it circular
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        
        # If the list is not empty, traverse to the end of the list and add the new node
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head
        
    def manipulate_node(self, new_data):
        # If the list is empty, do nothing
        if self.head is None:
            return
        
        # Traverse the list to find the central node (if there are an even number of nodes, use the second node from the middle as the central node)
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr.next != self.head and fast_ptr.next.next != self.head:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # Manipulate the data of the central node
        slow_ptr.data = new_data
        
    def delete_current_node(self):
        # If the list is empty, do nothing
        if self.head is None:
            return
        
        # If the list has only one node, set the head to None
        if self.head.next == self.head:
            self.head = None
            return
        
        # Traverse the list to find the current node (the node before the head)
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        
        # Delete the current node by setting its next to the head and updating the head
        current_node.next = self.head.next
        self.head = current_node.next
        
    def print_list(self):
        # Traverse the list starting from the head and print each node's data
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()

# Create a new circular linked list and append some nodes
my_list = LinkedList()
my_list.append(11)
my_list.append(12)
my_list.append(13)
my_list.append(14)
my_list.append(15)

# Print the initial list
print("Initial list:")
my_list.print_list()

# Manipulate the central node
my_list.manipulate_node(20)
print("After manipulating a node:")
my_list.print_list()

# Delete the current node
my_list.delete_current_node()
print("After deleting a node:")
my_list.print_list()

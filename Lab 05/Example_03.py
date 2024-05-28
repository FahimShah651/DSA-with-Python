# Define a class for the doubly linked list node
class Node_of_doubly_linked_list:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Define a class for the doubly linked list
class a_Doubly_Linked_List:
    def __init__(self):
        self.head = None
    
    # Function to add a new node at the end of the list
    def append(self, data):
        new_node = Node_of_doubly_linked_list(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
    
    # Function to display the contents of the list
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

# Example usage
my_list = a_Doubly_Linked_List()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()

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
        self.tail = None
    
    # Method to add a new node with data to the front of the list
    def next_of_node(self, data):
        new_node = Node_of_doubly_linked_list(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.print_list()
    
    # Method to add a new node with data to the back of the list
    def prev_of_node(self, data):
        new_node = Node_of_doubly_linked_list(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.print_list()
    
    # Method to remove and return data from the first node in the list
    def remove_next(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.print_list()
        return data
    
    # Method to remove and return data from the last node in the list
    def remove_prev(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.print_list()
        return data
    
    # Method to print the list
    def print_list(self):
        current_node = self.head
        print("List contents: ", end="")
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Example usage
my_list = a_Doubly_Linked_List()

my_list.prev_of_node(11)
my_list.next_of_node(10)
my_list.prev_of_node(12)
my_list.next_of_node(9)

my_list.remove_next()
my_list.remove_prev()

my_list.prev_of_node(5)
my_list.next_of_node(6)

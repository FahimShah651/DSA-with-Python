class Double_Ended_Queue:

    def __init__(self):
        """Initialize a Deque object with a fixed capacity"""
        self.arr = []   # Circular array to hold the elements

    def is_empty(self):
        """Check if the deque is empty"""
        return len(self.arr) == 0

    def get_front(self):
        """Get the value of the front element"""
        if self.is_empty():
            return None
        else:
            return self.arr[0]
    
    def insert_front(self, value):
        """Insert an element at the front of the deque""" 
        self.arr.insert(0,value)
      
    def delete_front(self):
        """Delete the element at the front of the deque"""
        if self.is_empty():
            return False  # Return False if deque is already empty
        else:
            self.arr.pop(0)
       
    def display(self):
        return self.arr
    
    def insert_back(self,value):
        self.arr.append(value)
        
    def delete_back(self):
        self.arr.pop(-1)
        

# Create a deque with a capacity of 4
d = Double_Ended_Queue()
print("Insert at front :")
d.insert_front(1)
d.insert_front(2)
d.insert_front(3)
print(d.display())
print("\nInsert at back :")
d.insert_back(4)
d.insert_back(5)
d.insert_back(6)
print(d.display())

print("\nDelete from front: ")
d.delete_front()
print(d.display())

print("\nDelete from back: ")
d.delete_back()
print(d.display())

print("\nGet from front: ")
print(d.get_front())


print("Is list empty:", d.is_empty(),"\n")

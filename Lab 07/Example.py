class ArrayQueue:
    DEFAULT_CAPACITY = 5    # The default capacity of the queue.
    
    def __init__(self):
        # Initialize the queue with the default capacity.
        self.data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        # Return the number of elements in the queue.
        return self.size

    def is_empty(self):
        # Return True if the queue is empty, False otherwise.
        return self.size == 0

    def dequeue(self):
        if self.size > 0 : 
          del(self.data[0])
          self.size = self.size - 1

    def enqueue(self, e):
        # Add an element to the back of the queue.
        if self.size == len(self.data):
            # Resize the array if it is full.
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def resize(self, cap): # Resize the array to the specified capacity.
        old = self.data  
        self.data = [None] * cap  
        walk = self.front
        for k in range(self.size):  
            self.data[k] = old[walk]  
            walk = (1 + walk) % len(old) 
        self.front = 0  

    def print(self):        # Print the contents of the queue.
        if self.is_empty():
            print("Queue is empty")
        else:
            print("[",end="")
            for i in range(0,len(self.data)):
               if self.data[i] != None :
                 print(f" {self.data[i]} ",end="")
               if i <= (self.size-2):
                 print(",",end="")
            print("]")
       


# Make code for the main
myQ = ArrayQueue()

print("\n")
for i in range(1,8):
    myQ.enqueue(i*10)
print("Elements After Enqueue : ",end="")
myQ.print()
for i in range(1,8):
    myQ.dequeue()
    print(i," Time Dequeue Called : ",end="")
    myQ.print()
    
print("\n")
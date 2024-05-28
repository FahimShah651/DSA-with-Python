class ArrayQueue:
    # This class implements a queue using an array.

    DEFAULT_CAPACITY = 5  # The default capacity of the queue.

    def __init__(self):
        # Initialize the queue with the default capacity.
        self.data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0  # The number of elements in the queue.
        self.front = 0  # The index of the front element of the queue.

    def __len__(self):
        # Return the number of elements in the queue.
        return self.size

    def is_empty(self):
        # Return True if the queue is empty, False otherwise.
        return self.size == 0

    def first(self):
        # Return the first element of the queue.
        # Raises an exception if the queue is empty.
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front]

    def dequeue(self):
        # Remove and return the first element of the queue.
        # Raises an exception if the queue is empty.
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def enqueue(self, e):
        # Add an element to the back of the queue.
        if self.size == len(self.data):
            # Resize the array if it is full.
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def resize(self, cap):
        # Resize the array to the specified capacity.
        old = self.data
        self.data = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0

    def print(self):
        # Print the contents of the queue.
        print("[", end="")
        for i in range(0, len(self.data)):
            if self.data[i] != None:
                print(f" {self.data[i]} ", end="")
            if i <= (self.size - 2):
                print(",", end="")
        print("]")


# Make code for the main
myQ = ArrayQueue()

myQ.enqueue(10)
myQ.enqueue(20)
myQ.enqueue(30)
myQ.enqueue(40)
myQ.enqueue(50)
myQ.enqueue(60)
myQ.print()
myQ.dequeue()
myQ.print()
myQ.dequeue()
myQ.print()

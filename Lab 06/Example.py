class ArrayStack:
    # LIFO Stack implementation using a Python list as underlying storage.
    def __init__(self):
        # Create an empty stack.
        self._data = [] # nonpublic list instance

    def __len__(self):
        # Return the number of elements in the stack.
        return len(self._data)

    def is_empty(self):
        # Return True if the stack is empty.
        return len(self._data) == 0

    def push(self, e):
        # Add element e to the top of the stack.
        self._data.append(e) # new item stored at end of list

    def top(self):
        '''Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1] # the last item in the list

    def pop(self):
        '''Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop() # remove last item from list


# Create a new stack instance
stack = ArrayStack()

# Push some elements onto the stack
stack.push(100)
stack.push(200)
stack.push(300)

# Print the length of the stack (should be 3)
print(len(stack))

# Print the top element of the stack (should be 3)
print(stack.top())

# Pop the top element off the stack (should return 3)
print(stack.pop())

# Print the length of the stack (should be 2)
print(len(stack))

# Pop the remaining elements off the stack (should return 2)
print(stack.pop())

# Print the length of the stack (should be 1)
print(len(stack))

# Pop the remaining elements off the stack (should return 2)
print(stack.pop())
print(stack.pop())
# Print whether the stack is empty (should be True)
print(stack.is_empty())

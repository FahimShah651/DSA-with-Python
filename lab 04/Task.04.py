class DynamicArray:
    def __init__(self):
        self.array = []
    
    def insert(self, val):
        self.array.append(val)
    
    def display(self):
        print("Dynamic Array : ", self.array)

def unique_elements(arr):
    # Create a new empty array
    unique_arr = []

    # Iterate over the original array
    for element in arr:
        # Check if the element is already in the new array
        if element not in unique_arr:
            # Add the element to the new array if it's not already there
            unique_arr.append(element)

    # Return the new array with unique elements
    return unique_arr


# Create an object of the DynamicArray class
my_array = DynamicArray()

# Take input from the user and add elements to the array
n = int(input("Enter the size of the array : "))
for i in range(n):
    val = int(input(f"Enter the {i+1} element : "))
    my_array.insert(val)

# Display the original array
my_array.display()

# Get a new array with unique elements
unique_arr = unique_elements(my_array.array)

# Display the new array with unique elements
print("New Array with Unique Elements : ", unique_arr)

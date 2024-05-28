import array

# Define a function to take input from the user and add elements to an array
def input_user(n,arr):
    for i in range(n):
        # Prompt user to enter each element of the array
        elem = int(input(f"Enter the {i+1} element : " ))
        # Add the element to the array
        arr.append(elem)

# Prompt the user to enter the size of the array
n = int(input("Enter the size of array : "))

# Create an empty array of integers using the "i" type code
my_array = array.array("i",[])

# Call the input_user() function to get input from the user and add elements to the array
input_user(n, my_array)

# Print the original array
print("Original array : ", my_array)

# Reverse the array
my_array.reverse()

# Print the reversed array
print("Reversed array : ", my_array)



# Print the sorted array
print("Sorted array : ",sorted(my_array))

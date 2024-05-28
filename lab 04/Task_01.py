# Import the array module
import array

# Import all classes and functions from the array module
from array import*

# Define a function to take input from user and add elements to an array
def input_user(n,arr):
    for i in range(n):
        # Prompt user to enter each element of the array
        elem = int(input(f"Enter the {i+1} element : " ))
        # Add the element to the array
        arr.append(elem)
        
# Define a function to calculate the average of an array
def avg(arr):
    # Calculate the sum of the array and divide by the length of the array to get the average
    return (sum(arr)/len(arr))

# Prompt the user to enter the size of the array
n = int(input("enter the size of array : "))

# Create an empty array of integers using the "i" type code
my_array = array("i",[])

# Call the input_user() function to get input from the user and add elements to the array
input_user(n,my_array)

# Print the array
print("The array is :  " ,my_array)

# Print the sum of the elements in the array
print(f"the sum of the array is : {sum(my_array)}")

# Print the average of the elements in the array
print(f"the average is : {avg(my_array)}")

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

# Define a function to sort an array
def my_sort(arr):
    n = len(arr)
    # Implement bubble sort algorithm to sort the array in ascending order
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # Return the sorted array
    return arr

# Create an empty array of integers using the "i" type code
my_array = array("i",{})

# Prompt the user to enter the size of the array
n = int(input("enter the size of array : "))

# Call the input_user() function to get input from the user and add elements to the array
input_user(n,my_array)

# Print the original array
print(f"My  array  is   : {my_array}")

# Call the my_sort() function to sort the array
my_sort(my_array)

# Print the sorted array
print(f"Sorted array is : {my_array}")

# Print the smallest element of the array
print(f"Smallest Number is : {my_array[0]}")

# Print the largest element of the array
print(f"Greatest Number is : {my_array[len(my_array)-1]}")

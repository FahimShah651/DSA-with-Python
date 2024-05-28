""" 
Task 2: Suppose you have to input a list of ten numbers and you want to
calculate the summ of all the even numbers in the list. Make the program using for
loop without index. 



num_list = []
summ = 0
for i in range(1,11):
    x = int(input(f"Enter the  {i}  Number : "))
    num_list.append(x)
    if(x%2 ==0):
        summ +=x

print(f"The list of the Input Numbers is : \n {num_list}")
print(f"\n The summ of the Even Numbers is : {summ}")

"""


num_list = []          # empty list to store numbers
summ = 0               # variable to store the sum
for i in range(1,11):  # for loop to enter 10 numbers
    x = int(input(f"Enter the {i} Number: "))   # user enter the i-th number
    num_list.append(x)                          # Add the number to the list of input numbers
    
    # Check if the number is even and add it to the sum of even numbers if it is
    if(x%2 == 0):
        summ += x

# Print the list of input numbers
print(f"The list of the Input Numbers is: \n {num_list}")

# Print the sum of even numbers in the list
print(f"\nThe sum of the Even Numbers is: {summ}")



# Define a function that calculates the area of a rectangle
def Area_of_Rectangle(LENGTH: float, WIDTH: float) -> float:
    area = LENGTH * WIDTH  # Calculate the area
    return area

# Prompt the user to enter the length and width of the rectangle
len_enter = float(input("Enter the Length of the rectangle: "))
wid_enter = float(input("Enter the Width of the rectangle: "))

# Call the function to calculate the area and print the result
print(f"The Area of Rectangle is: {Area_of_Rectangle(len_enter, wid_enter)}")

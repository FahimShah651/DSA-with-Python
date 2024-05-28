
# user enter the number of prices to be entered
number_of_prices = int(input("Enter The Number of Prices: "))
# Initialize an empty list to store the prices
Price_List = []
# Use a for loop to prompt the user to enter each price and append it to the list
for i in range(1, number_of_prices+1):
    price = int(input(f"Enter the {i} Price: "))
    Price_List.append(price)

# Print the list of prices
print(f"The Price List is {Price_List}")

# Sort the list in descending order and print the highest price
Price_List.sort(reverse=True)
print(f"The Highest Price in The List is: {Price_List[0]}")

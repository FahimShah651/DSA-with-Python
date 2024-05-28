
# User enter  salary and budget limit
salary = float(input("Enter Your Salary: "))
budget_limit = float(input("Enter Your Budget Limit: "))

#  User enter spending amounts until their remaining salary falls below their budget limit
while salary >= budget_limit:
    spent = float(input("Enter The Amount you want to Spend: "))
    
    # Check if the user has enough salary to cover the spending amount
    if spent <= salary:
        salary -= spent
    else:
        # If the user does not have enough salary to cover the spending amount, break out of the loop
        print("Sorry, Your Account Is with Low Balance.")
        break
    
# Once the user's remaining salary falls below their budget limit, output a message indicating that their budget limit has been reached
print("Thanks For Shopping, Your Budget Limit Has Been Reached.")


# Define a function that takes in two numbers and returns their product
def Multiplication(num1:float,num2:float):
    return (num1*num2)

# Define a main function that asks the user for two numbers, calls the Multiplication function, and prints the result
def main():
  first_num  = float(input("Enter First Number  :"))
  second_num = float(input("Enter Second Number :"))
  print(f"The Product of {first_num} and {second_num} is: {Multiplication(first_num, second_num)}")

if __name__ =='__main__':
   main()

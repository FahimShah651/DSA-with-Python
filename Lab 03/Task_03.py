# Open the file for reading
with open("My Text File.txt", "r") as file:
    content = file.read()

# Print the initial content of the file
print("\n\n\nInitial content of the file:")
print(content)

# Open the file for writing and append new text
with open("My Text File.txt", "a") as file:
    file.write("\nThis is new text appended to the file.")

# Open the file for reading again
with open("My Text File.txt", "r") as file:
    content = file.read()

# Print the final content of the file
print("\n\n\nFinal content of the file:")
print(content,"\n\n\n")

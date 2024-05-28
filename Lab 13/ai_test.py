# from tkinter import *
# import sqlite3
# root = Tk()
# root.title("Library Management System")
# root.geometry("800x400")
# conn = sqlite3.connect("library.db")
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)")
# def add_book():
#     # Retrieve data from input fields
#     title = title_entry.get()
#     author = author_entry.get()
#     year = year_entry.get()
    
#     # Insert book into the database
#     cursor.execute("INSERT INTO books VALUES (NULL, ?, ?, ?)", (title, author, year))
    
#     # Commit changes and clear input fields
#     conn.commit()
#     title_entry.delete(0, END)
#     author_entry.delete(0, END)
#     year_entry.delete(0, END)

# def search_book():
#     # Retrieve search keyword
#     keyword = search_entry.get()
    
#     # Search books in the database
#     cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR year LIKE ?", ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
    
#     # Clear previous search results
#     search_listbox.delete(0, END)
    
#     # Display search results
#     for book in cursor.fetchall():
#         search_listbox.insert(END, book)

# # Implement similar functions for update and delete operations
# # Create labels
# title_label = Label(root, text="Title")
# author_label = Label(root, text="Author")
# year_label = Label(root, text="Year")

# # Create entry fields
# title_entry = Entry(root)
# author_entry = Entry(root)
# year_entry = Entry(root)

# # Create buttons
# add_button = Button(root, text="Add Book", command=add_book)
# search_button = Button(root, text="Search", command=search_book)

# # Create search results listbox
# search_listbox = Listbox(root, width=70)

# # Layout components using grid layout manager
# title_label.grid(row=0, column=0)
# author_label.grid(row=1, column=0)
# year_label.grid(row=2, column=0)

# title_entry.grid(row=0, column=1)
# author_entry.grid(row=1, column=1)
# year_entry.grid(row=2, column=1)

# add_button.grid(row=3, column=0)
# search_button.grid(row=4, column=1)

# search_listbox.grid(row=5, columnspan=2)
# def close_app():
#     # Close database connection and destroy the main window
#     conn.close()
#     root.destroy()

# root.protocol("WM_DELETE_WINDOW", close_app)
# root.mainloop()
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def get_numbers():
    numbers = []
    num_count = int(input("How many numbers do you want to enter? "))
    for i in range(num_count):
        number = float(input("Enter number {}: ".format(i+1)))
        numbers.append(number)
    return numbers

def main():
    numbers = get_numbers()
    average = calculate_average(numbers)
    print("The average is:", average)

# Run the program
main()

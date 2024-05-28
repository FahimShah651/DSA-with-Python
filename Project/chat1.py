from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, END

class LibraryCatalog:
    def __init__(self):
        self.books = []
        self.root = Tk()
        self.root.title("Library Catalog System")

        self.title_label = Label(self.root, text="Title")
        self.title_label.grid(row=0, column=0)
        self.title_entry = Entry(self.root)
        self.title_entry.grid(row=0, column=1)

        self.author_label = Label(self.root, text="Author")
        self.author_label.grid(row=1, column=0)
        self.author_entry = Entry(self.root)
        self.author_entry.grid(row=1, column=1)

        self.subject_label = Label(self.root, text="Subject")
        self.subject_label.grid(row=2, column=0)
        self.subject_entry = Entry(self.root)
        self.subject_entry.grid(row=2, column=1)

        self.add_button = Button(self.root, text="Add Book", command=self.add_book)
        self.add_button.grid(row=3, column=0)

        self.remove_button = Button(self.root, text="Remove Book", command=self.remove_book)
        self.remove_button.grid(row=3, column=1)

        self.search_button = Button(self.root, text="Search", command=self.search_books)
        self.search_button.grid(row=4, column=0, columnspan=2)

        self.results_listbox = Listbox(self.root, width=50)
        self.results_listbox.grid(row=5, column=0, columnspan=2)

        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.grid(row=5, column=2, sticky="NS")
        self.results_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.results_listbox.yview)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        subject = self.subject_entry.get()
        book = {"title": title, "author": author, "subject": subject, "available": True}
        self.books.append(book)
        self.clear_entries()

    def remove_book(self):
        selected_index = self.results_listbox.curselection()
        if selected_index:
            del self.books[selected_index[0]]
            self.display_books()

    def search_books(self):
        query = self.title_entry.get()
        search_results = []
        for book in self.books:
            if query.lower() in book["title"].lower() or query.lower() in book["author"].lower() or query.lower() in book["subject"].lower():
                search_results.append(book)
        self.display_books(search_results)

    def display_books(self, books=None):
        self.results_listbox.delete(0, END)
        if not books:
            books = self.books
        for book in books:
            availability = "Available" if book["available"] else "Not Available"
            self.results_listbox.insert(END, f"{book['title']} by {book['author']} ({availability})")

    def clear_entries(self):
        self.title_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.subject_entry.delete(0, END)

    def run(self):
        self.root.mainloop()

# Create an instance of the LibraryCatalog and run the program
catalog = LibraryCatalog()
catalog.run()

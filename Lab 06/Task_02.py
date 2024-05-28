"""
class library():
    def __init__(self) :
        self.stack = []
        self.s = "/ab/cd/\\efg\\hij/"
    
    def rearrange_library(self):
    
     for i in range(len(self.s)):
        if self.s[i] == '/':
            continue
        elif self.s[i] == '\\':
            if len(self.stack) > 0:
                self.stack.pop()
        else:
            self.stack.append(self.s[i])
     return ''.join(self.stack)

book_1 = library

# s = "/ab/cd/\\efg\\hij/"
print(book_1.rearrange_library()) # "jihgfedcba"

        
        """
class BookStack:
    def __init__(self):
        self.stack = []

    def add_book(self, book):
        self.stack.append(book)

    def reverse_order(self):
        reversed_books = []
        while self.stack:
            reversed_books.append(self.stack.pop())
        return reversed_books

# Example usage:
shelf = "/abcde\\"
book_stack = BookStack()

# Add books to the stack
for book in shelf[1:-1]:
    book_stack.add_book(book)

# Print the reversed order of books
print(book_stack.reverse_order())

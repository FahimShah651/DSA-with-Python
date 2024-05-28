class TicketBookingSystem:
    def __init__(self):
        """Initialize a TicketBookingSystem object"""
        self.seats = []   # List to hold the seats

    def is_empty(self):
        """Check if the booking system is empty"""
        return len(self.seats) == 0
    
    def book_front(self, name):
        """Book a seat at the front of the booking system""" 
        self.seats.insert(0, name)
      
    def cancel_front(self):
        """Cancel the seat at the front of the booking system"""
        if self.is_empty():
            return False  # Return False if the booking system is already empty
        else:
            self.seats.pop(0)
       
    def display(self):
        """Display the seats in the booking system"""
        return self.seats
    
    def book_back(self, name):
        """Book a seat at the back of the booking system"""
        self.seats.append(name)
        
    def cancel_back(self):
        """Cancel the seat at the back of the booking system"""
        self.seats.pop(-1)
    
    def get_total_tickets(self):
        """Get the total number of booked seats"""
        return len(self.seats) 

# Create a booking system
booking_system = TicketBookingSystem()
print("Book Seat at front:")
booking_system.book_front("Muhammad")
booking_system.book_front("Ahmed")
booking_system.book_front("Fatima")
print(booking_system.display())
print("\nBook Seat at back:")
booking_system.book_back("Ali")
booking_system.book_back("Aisha")
booking_system.book_back("Yusuf")
print(booking_system.display())

print("\nCancel Seat from front:")
booking_system.cancel_front()
print(booking_system.display())

print("\nCancel Seat from back:")
booking_system.cancel_back()
print(booking_system.display())

print("Total Tickets:", booking_system.get_total_tickets(), "\n")

class ChocolateStack:
    def __init__(self):
        self.stack = []

    def chocolates_sold(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def chocolates_available(self, n_chocolates):
        self.stack.append(n_chocolates)

    def get_total_chocolates(self):
        return sum(self.stack)

    def get_number_of_boxes(self):
        return len(self.stack)


chocolate_stack = ChocolateStack()

chocolate_stack.chocolates_available(10)
chocolate_stack.chocolates_available(20)
chocolate_stack.chocolates_available(30)

print("Choclate boxes",chocolate_stack.get_number_of_boxes()) # 3
print("Total Choclates",chocolate_stack.get_total_chocolates()) # 60

sold_chocolates = chocolate_stack.chocolates_sold()
print("Sold Choclates ",sold_chocolates) # 30

print("Choclate boxes",chocolate_stack.get_number_of_boxes()) # 2
print("Total Choclates",chocolate_stack.get_total_chocolates()) # 40

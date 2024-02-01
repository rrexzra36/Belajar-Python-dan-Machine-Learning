class Cashier:
    def __init__(self):
        self.total_cost = 0.0
        self.cash_received = 0.0
        self.change = 0.0

    def add_item_cost(self, cost):
        self.total_cost += cost

    def receive_cash(self, cash):
        self.cash_received += cash

    def calculate_change(self):
        self.change = self.cash_received - self.total_cost

    def get_change(self):
        return self.change


cashier = Cashier()

# Add the cost of each item to the total cost
while True:
    item_cost = input("Enter item cost (Enter 'q' to quit): ")
    if item_cost == 'q':
        break
    cashier.add_item_cost(float(item_cost))

# Receive cash from the customer
cash_received = float(input("Enter cash received: "))
cashier.receive_cash(cash_received)

# Calculate and return the change
cashier.calculate_change()
print("Change: $" + str(cashier.get_change()))
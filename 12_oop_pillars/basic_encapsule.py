class Wallet:
    
    # Basic idea of encapsulation:
    # Keep the data and the methods related to that data
    # together inside the same class.
    
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
    
    # These methods work with the wallet's balance,
    # so they are kept inside the Wallet class.
   
    #method to add money
    def add_money(self,amount):
        self.balance += amount
        
    #method to spend money
    def spend_money(self,amount):
        self.balance -= amount
        
    def show_balance(self):
        print(f"Current balance = Rs {self.balance}")
        
wal1 = Wallet("Priyam",5000)
wal1.add_money(2000)
wal1.spend_money(1500)
wal1.show_balance()



# Encapsulation means keeping data and related methods
# together inside a class.
#
# In this example:
# Data    → owner_name, balance
# Methods → add_money(), spend_money(), show_balance()
#
# All of them are kept inside the Wallet class.
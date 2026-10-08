
class Wallet:
    
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance        #private attribute

    #method to add money
    def add_money(self,amount):
        self.__balance += amount
        
    #method to spend money
    def spend_money(self,amount):
        self.__balance -= amount
        
    def show_balance(self):
        print(f"Current balance = Rs {self.__balance}")
        
wal1 = Wallet("Priyam",5000)
wal1.add_money(2000)
wal1.spend_money(1500)
wal1.show_balance()








class BankAccount:
    
    def __init__(self,balance):
        self.__balance = balance
        
    def add_money(self,amount):
        self.__balance += amount
        
    def show_balance(self):
        print(f"Total balance = Rs {self.__balance}")
        
acc1 = BankAccount(5000)
acc1.add_money(2000)
acc1.show_balance()


# Wallet + BankAccount
# Concept:
# - __balance → private attribute
# - Direct access → ❌ Not allowed
# - Modify balance through methods → ✅
# - add_money() → updates the private data
# - spend_money() → updates the private data
# - show_balance() → reads the private data
# Topic: Private Data + Controlled Modification 🔒
